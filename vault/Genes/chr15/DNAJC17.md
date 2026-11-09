---
symbol: "DNAJC17"
type: "gene"
col: 2416
ensembl_id: "ENSG00000104129"
name: "DnaJ heat shock protein family (Hsp40) member C17"
location: "15q15.1"
module: 36
arm: "+"
pooled_cpm: 16.57
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# DNAJC17

*DnaJ heat shock protein family (Hsp40) member C17* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.65× (z +9.4, q 2e-18, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.554× (z -15.7, q 0e+00, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT61B]] (+0.65, fdr 2e-05), [[SLC25A17]] (+0.62, fdr 3e-05), [[PCGF6]] (+0.62, fdr 1e-05); moves opposite to [[TLE4]] (-0.51, fdr 3e-05), [[PPP1R15B]] (-0.50, fdr 5e-05), [[TLL2]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2416.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +9.4 | 2e-18 | 37/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +6.5 | 3e-08 | 21/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +6.0 | 3e-07 | 25/48 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.8 | 0.019 | 12/47 (LOX-IMVI, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2416.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.554×** | -15.7 | 0e+00 | 36/47 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.436×** | -15.6 | 0e+00 | 42/48 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.458×** | -14.7 | 0e+00 | 44/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.596×** | -9.7 | 4e-20 | 34/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -8.3 | 2e-14 | 30/46 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.673×** | -7.3 | 3e-11 | 25/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.780×** | -6.6 | 3e-09 | 22/48 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -6.6 | 3e-09 | 24/46 (Hs 766T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -6.2 | 3e-08 | 23/44 (LS 180, C-33 A, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -6.1 | 5e-08 | 28/48 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.723×** | -6.1 | 6e-08 | 23/46 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.729×** | -5.7 | 5e-07 | 18/31 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.773×** | -4.8 | 6e-05 | 15/40 (A549, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.766×** | -4.6 | 2e-04 | 14/34 (HCT15, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.806×** | -3.9 | 0.004 | 14/47 (NCI-H1792, AN3 CA, …) | rises with dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.674×** | -3.9 | 0.004 | 16/45 (SW48, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.815×** | -3.8 | 0.004 | 12/47 (CHP-212, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.689×** | -3.7 | 0.007 | 8/48 (SW1417, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.715×** | -3.3 | 0.028 | 11/45 (SNU-1, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2416. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.0 | 2 | 2 | [[Ixazomib citrate (drug)]] 5 µM 3.13× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.8) |
| [[A-172 (line)]] | wt | 18.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 31.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.368× (z -8.8) |
| [[SW1417 (line)]] | alt | 25.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -10.2) |
| [[C32 (line)]] | wt | 16.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0947× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.308× (z -9.3) |
| [[HCT15 (line)]] | alt | 25.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0512× (z -8.8) |
| [[LS 180 (line)]] | wt | 16.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.164× (z -12.2) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 21.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.228× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 14.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -9.4) |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.8) |
| [[A-427 (line)]] | wt | 12.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0833× (z -14.1) |
| [[A498 (line)]] | wt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -8.5) |
| [[A549 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0881× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[C-33 A (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[CFPAC-1 (line)]] | alt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -10.4) |
| [[COLO 205 (line)]] | alt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.112× (z -8.8) ⚠ toxic; unreliable plate only |
| [[HOP62 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -12.2) |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -9.5) |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.112× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 16.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -9.0) |
| [[AN3 CA (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2416), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT61B]] | +0.65 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[SLC25A17]] | +0.62 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[PCGF6]] | +0.62 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[TOMM40L]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TMLHE]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[TEFM]] | +0.59 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[GTF3C2]] | +0.58 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ZNF875]] | +0.58 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[L3MBTL2]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[PARGP1]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[NDUFAF5]] | +0.57 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[SPHK2]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLE4]] | -0.51 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R15B]] | -0.50 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[TLL2]] | -0.49 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[MYBL1]] | -0.49 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[ATF3]] | -0.48 | -0.56 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers DNAJC17's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.462). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-43.1, 9.7); signed map (-18.0, -21.8). **Vector** length 73.6, 12.6% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.7 | +9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.4 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.1 | -0.2 |
| fall | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.6 | -6.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.4 | -2.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.2 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -3.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,765,161-40,807,478 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10634 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins; RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVM6](https://www.uniprot.org/uniprotkb/Q9NVM6) (DnaJ homolog subfamily C member 17):

> May negatively affect PAX8-induced thyroglobulin/TG transcription.

**Summary**, from NCBI Gene [55192](https://www.ncbi.nlm.nih.gov/gene/55192):

> Predicted to enable RNA binding activity. Predicted to be involved in spliceosomal complex disassembly. Predicted to act upstream of or within negative regulation of transcription by RNA polymerase II. Predicted to be located in cytoplasm and nucleus. Predicted to be part of spliceosomal complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25556) · Entrez [55192](https://www.ncbi.nlm.nih.gov/gene/55192) · UniProt [Q9NVM6](https://www.uniprot.org/uniprotkb/Q9NVM6) · Ensembl [ENSG00000104129](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104129)

## Data

Gene col 2416: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2416); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2416, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2416]; `tensor/DDL_lfc|DDL_z.npy` [2416]; `embed/gene_vectors.npy` [2416]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2416 or target_col == 2416). Every well: [[DNAJC17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
