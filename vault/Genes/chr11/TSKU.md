---
symbol: "TSKU"
type: "gene"
col: 11316
ensembl_id: "ENSG00000182704"
name: "tsukushi, small leucine rich proteoglycan"
location: "11q13.5"
module: 20
arm: "+"
pooled_cpm: 11.69
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 34
n_dd_up_clean: 0
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# TSKU

*tsukushi, small leucine rich proteoglycan* — 11q13.5

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.203× (z -31.6, q 0e+00, down in 39 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COASY]] (+0.54, fdr 3e-05), [[PSMA6]] (+0.51, fdr 2e-05), [[CUL2]] (+0.51, fdr 2e-05); moves opposite to [[LRCH3]] (-0.58, fdr 1e-05), [[JMJD1C]] (-0.55, fdr 4e-05), [[CEP135]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCL20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11316.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.32 | 9/46 (A549, A498, …) | inconsistent across doses |  |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | 1.27× | +3.1 | 0.32 | 7/43 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 1.27× | +3.1 | 0.32 | 5/45 (HOP62, CFPAC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11316.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.203×** | -31.6 | 0e+00 | 39/41 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.215×** | -21.5 | 0e+00 | 39/41 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.321×** | -15.9 | 0e+00 | 40/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.315×** | -15.6 | 0e+00 | 38/45 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.358×** | -14.4 | 6e-45 | 38/46 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.391×** | -13.2 | 2e-37 | 35/46 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.588×** | -10.5 | 6e-24 | 27/41 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.512×** | -9.4 | 5e-19 | 33/47 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.581×** | -7.6 | 2e-12 | 29/42 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.698×** | -7.1 | 6e-11 | 25/46 (LS 180, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.610×** | -6.9 | 2e-10 | 20/46 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.614×** | -6.8 | 4e-10 | 28/44 (A549, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.624×** | -6.6 | 2e-09 | 24/47 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -6.5 | 3e-09 | 21/40 (HT-29, HOP62, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.663×** | -5.8 | 3e-07 | 19/45 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.725×** | -4.3 | 4e-04 | 12/44 (AN3 CA, CFPAC-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.743×** | -4.2 | 9e-04 | 17/46 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 28.9 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0711× (z -26.8) |
| [[NCI-H460 (line)]] | wt | 21.9 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0657× (z -20.7) |
| [[A549 (line)]] | wt | 33.1 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0307× (z -25.7) |
| [[A498 (line)]] | wt | 23.2 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -20.1) |
| [[HOP62 (line)]] | alt | 9.02 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -16.4) |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0970× (z -18.6) |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0620× (z -24.4) |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -19.1) |
| [[KATO III (line)]] | alt | 9.42 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.262× (z -9.5) |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 5.36 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0961× (z -11.0) |
| [[SW480 (line)]] | alt | 6.09 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0753× (z -23.5) |
| [[HEC-1-A (line)]] | alt | 8.49 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -16.8) |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0533× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -14.6) |
| [[PANC-1 (line)]] | alt | 4.90 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0828× (z -19.0) |
| [[RPMI-7951 (line)]] | alt | 17.3 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0562× (z -13.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.147× (z -13.3) |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.239× (z -9.3) |
| [[H4 (line)]] | wt | 21.8 | 0 | 2 | — | [[Peretinoin (drug)]] 0.5 µM 0.0883× (z -9.9) |
| [[J82 (line)]] | alt | 13.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -17.2) |
| [[LoVo (line)]] | wt | 6.58 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0631× (z -21.2) |
| [[NCI-H2030 (line)]] | alt | 5.50 | 0 | 2 (1 ⚠) | — | [[Ornidazole (drug)]] 0.5 µM 0.0460× (z -12.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -8.6) |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -14.0) |
| [[SW 900 (line)]] | alt | 9.57 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0400× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 7.28 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0889× (z -18.6) |
| [[HCT15 (line)]] | alt | 6.60 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -8.7) |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 5.69 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0780× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0811× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 6.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0518× (z -12.8) |
| [[A-427 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COASY]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[PSMA6]] | +0.51 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[CUL2]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ZNF174]] | +0.48 | +0.40 / +0.37 | both halves | 8e-05 |  |
| [[ZDHHC16]] | +0.48 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[MINPP1]] | +0.48 | +0.42 / +0.23 | both halves | 5e-04 |  |
| [[TNFRSF1A]] | +0.48 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ALKBH5]] | +0.47 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[SCARB2]] | +0.47 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[USF1]] | +0.47 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[DAG1]] | +0.46 | +0.53 / +0.32 | both halves | 2e-04 |  |
| [[ADAM15]] | +0.46 | +0.63 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRCH3]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[JMJD1C]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[CEP135]] | -0.55 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[PPP3CB]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[MYSM1]] | -0.47 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[OFD1]] | -0.47 | -0.59 / -0.29 | both halves | 2e-04 |  |
| [[ARMH4]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[CHMP4A]] | -0.46 | -0.56 / -0.29 | both halves | 3e-04 |  |
| [[MYL12A]] | -0.45 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[TSG101]] | -0.45 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[HELQ]] | -0.44 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[ZSWIM4]] | -0.44 | -0.36 / -0.42 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCL20]] | B | CCL20 activity raises TSKU's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.33× lower at baseline in the lines without CCL20 | 0.069 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.328). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-43.6, -37.3); signed map (-36.6, -20.6). **Vector** length 68.9, 12.4% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.0 | +1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | -10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | -2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | -2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.4 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -15.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -21.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -31.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -9.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -4.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.8 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | tsukushi, small leucine rich proteoglycan |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.5 — chr11:76,782,251-76,798,153 (+) |
| Ensembl biotype | protein_coding |
| Also known as | E2IG4, TSK; previously LRRC54 |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUA8](https://www.uniprot.org/uniprotkb/Q8WUA8) (Tsukushi):

> Contributes to various developmental events and other processes such as wound healing and cholesterol homeostasis through its interactions with multiple signaling pathways. Wnt signaling inhibitor which competes with WNT2B for binding to Wnt receptor FZD4 and represses WNT2B-dependent development of the peripheral eye. Plays a role in regulating the hair cycle by controlling TGFB1 signaling. Required for the development of the anterior commissure in the brain by inhibiting neurite outgrowth. …

**Summary**, from NCBI Gene [25987](https://www.ncbi.nlm.nih.gov/gene/25987):

> Predicted to enable transforming growth factor beta binding activity. Predicted to be involved in several processes, including cholesterol efflux; cholesterol homeostasis; and nervous system development. Predicted to act upstream of or within several processes, including ciliary body morphogenesis; negative regulation of Wnt signaling pathway; and telencephalon development. Predicted to be located in obsolete extracellular space. Predicted to be active in gel phase of interstitial matrix. …

**Accessions** — [HGNC:28850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28850) · Entrez [25987](https://www.ncbi.nlm.nih.gov/gene/25987) · UniProt [Q8WUA8](https://www.uniprot.org/uniprotkb/Q8WUA8) · Ensembl [ENSG00000182704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182704)

## Data

Gene col 11316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11316); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11316]; `tensor/DDL_lfc|DDL_z.npy` [11316]; `embed/gene_vectors.npy` [11316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11316 or target_col == 11316). Every well: [[TSKU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSKU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
