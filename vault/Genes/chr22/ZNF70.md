---
symbol: "ZNF70"
type: "gene"
col: 11950
ensembl_id: "ENSG00000187792"
name: "zinc finger protein 70"
location: "22q11.23"
module: 49
arm: "+"
pooled_cpm: 7.13
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# ZNF70

*zinc finger protein 70* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.61× (z +5.9, q 2e-06, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.439× (z -10.2, q 9e-22, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.667× (z -4.8, q 9e-05, down in 20 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF526]] (+0.67, fdr 7e-06), [[ZNF417]] (+0.64, fdr 7e-06), [[ZNF17]] (+0.63, fdr 3e-05); moves opposite to [[RFX3]] (-0.54, fdr 2e-05), [[PTPRK]] (-0.52, fdr 3e-05), [[ERBIN]] (-0.51, fdr 6e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZNF568]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +5.9 | 2e-06 | 21/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.30×** | +4.6 | 0.001 | 18/48 (NCI-H2030, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 0.002 | 18/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11950.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.439×** | -10.2 | 9e-22 | 36/48 (HOP62, H4, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.468×** | -9.4 | 1e-18 | 29/44 (HOP62, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.614×** | -8.6 | 2e-15 | 26/45 (RPMI-7951, A498, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.571×** | -6.6 | 5e-09 | 27/46 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.582×** | -6.4 | 2e-08 | 25/46 (NCI-H1573, KATO III, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.604×** | -6.0 | 2e-07 | 22/36 (A-172, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.634×** | -5.4 | 4e-06 | 20/46 (A-172, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -4.8 | 9e-05 | 20/43 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.719×** | -4.1 | 0.002 | 17/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -4.0 | 0.004 | 15/43 (RKO, H4, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.717×** | -3.9 | 0.004 | 19/47 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.751×** | -3.6 | 0.017 | 16/47 (HS-578T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **0.674×** | -3.5 | 0.020 | 10/26 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.767×** | -3.1 | 0.071 | 11/46 (SNU-423, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.784×** | -3.0 | 0.092 | 15/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.23 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0802× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~36% of this change · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.104× (z -9.6) |
| [[HS-578T (line)]] | alt | 24.9 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -12.0) |
| [[A498 (line)]] | wt | 10.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -10.9) ⚠ cell-cycle shift, explains ~74% of this change |
| [[HOP62 (line)]] | alt | 7.79 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0394× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H460 (line)]] | wt | 8.36 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.173× (z -10.1) ⚠ cell-cycle shift, explains ~65% of this change |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -12.8) ⚠ cell-cycle shift, explains ~74% of this change |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 2 | — | [[Silodosin (drug)]] 5 µM 0.0669× (z -9.6) |
| [[C-33 A (line)]] | alt | 7.66 | 0 | 1 | — | [[Aliskiren (drug)]] 0.5 µM 0.0523× (z -9.8) |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0957× (z -9.6) |
| [[KATO III (line)]] | alt | 6.51 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0608× (z -10.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 4.56 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0950× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~16% of this change |
| [[MIA PaCa-2 (line)]] | alt | 8.26 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0643× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 5.34 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.101× (z -9.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2030 (line)]] | alt | 3.57 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0957× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 5.10 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0835× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RKO (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0886× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[SHP-77 (line)]] | alt | 9.09 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0731× (z -10.5) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.8) ⚠ cell-cycle shift, explains ~74% of this change |
| [[SW 900 (line)]] | alt | 9.96 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0992× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 5.24 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.161× (z -8.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF526]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 | same gene group |
| [[ZNF417]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 | same gene group |
| [[ZNF17]] | +0.63 | +0.64 / +0.44 | both halves | 3e-05 | same gene group |
| [[MSTO2P]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[RNF216P1]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RUSF1]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[COG1]] | +0.57 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[TSFM]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[RINT1]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SZT2]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[CCDC149]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NOMO2]] | +0.56 | +0.55 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX3]] | -0.54 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[PTPRK]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ERBIN]] | -0.51 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[SYNE2]] | -0.49 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[STAU2]] | -0.49 | -0.58 / -0.29 | both halves | 3e-04 |  |
| [[MAGI3]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[NFIB]] | -0.48 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[FRYL]] | -0.48 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[TMEM47]] | -0.47 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[PELI2]] | -0.47 | -0.47 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF568]] | B | ZNF568 activity raises ZNF70's level | lines that do not express ZNF568 (18) vs lines expressing it (32) | 1.55× lower at baseline in the lines without ZNF568 | 0.034 | ⚠ within organs, on part of the lines; also absent: ZNF829, ACTN2, ZNF880 |
| [[ZFP28]] | B | ZFP28 activity raises ZNF70's level | lines that do not express ZFP28 (21) vs lines expressing it (29) | 1.46× lower at baseline in the lines without ZFP28 | 0.036 | ⚠ within organs, on part of the lines; also absent: ZNF470, ZNF471, MAP6 |
| [[PELI2]] | B | PELI2 activity raises ZNF70's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 1.42× lower at baseline in the lines without PELI2 | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[BRSK1]] | B | BRSK1 activity raises ZNF70's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.71× lower at baseline in the lines without BRSK1 | 0.088 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.576). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.0, -29.7); signed map (-53.8, 2.7). **Vector** length 60.3, 8.40% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.2 | +1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | +3.2 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | +2.7 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.1 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.1 | +0.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.0 | +1.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.3 | -10.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.1 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -2.0 | -8.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.9 | -6.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -1.8 | -9.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.1 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -3.9 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 70 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:23,738,682-23,751,112 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cos17, MGC48959 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UC06](https://www.uniprot.org/uniprotkb/Q9UC06) (Zinc finger protein 70):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7621](https://www.ncbi.nlm.nih.gov/gene/7621):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in cytoplasm and megasporocyte nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13140) · Entrez [7621](https://www.ncbi.nlm.nih.gov/gene/7621) · UniProt [Q9UC06](https://www.uniprot.org/uniprotkb/Q9UC06) · Ensembl [ENSG00000187792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187792)

## Data

Gene col 11950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11950); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11950]; `tensor/DDL_lfc|DDL_z.npy` [11950]; `embed/gene_vectors.npy` [11950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11950 or target_col == 11950). Every well: [[ZNF70 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF70.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
