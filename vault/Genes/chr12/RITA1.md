---
symbol: "RITA1"
type: "gene"
col: 6302
ensembl_id: "ENSG00000139405"
name: "RBPJ interacting and tubulin associated 1"
location: "12q24.13"
module: 33
arm: "+"
pooled_cpm: 6.95
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# RITA1

*RBPJ interacting and tubulin associated 1* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.44× (z +10.6, q 2e-23, up in 11 of 14 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.49× (z +7.0, q 3e-10, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.558× (z -7.3, q 2e-10, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLAT]] (+0.71, fdr 7e-06), [[PHB1]] (+0.70, fdr 1e-05), [[BCS1L]] (+0.70, fdr 7e-06); moves opposite to [[TMEM91]] (-0.58, fdr 3e-05), [[PNISR]] (-0.54, fdr 4e-05), [[TSBP1-AS1]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[STEAP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6302.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.44×** | +10.6 | 2e-23 | 11/14 (SW1417, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.11×** | +9.2 | 9e-18 | 23/30 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.09×** | +9.1 | 2e-17 | 32/47 (J82, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.99×** | +8.5 | 3e-15 | 32/47 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.94×** | +7.6 | 4e-12 | 11/19 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.80×** | +7.2 | 5e-11 | 30/47 (A-172, AsPC-1, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +7.0 | 3e-10 | 23/46 (J82, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +5.9 | 3e-07 | 20/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.60×** | +5.5 | 2e-06 | 13/34 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +4.9 | 5e-05 | 23/43 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.31×** | +4.7 | 1e-04 | 19/42 (NCI-H460, A549, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +4.2 | 0.001 | 11/34 (LOX-IMVI, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +3.8 | 0.006 | 2/46 (PANC-1, A-172) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.011 | 7/42 (HT-29, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.027 | 6/47 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.62×** | +3.1 | 0.067 | 3/33 (NCI-H460, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.074 | 2/42 (BT-474, Hs 766T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6302.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.558×** | -7.3 | 2e-10 | 29/46 (SW1417, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.570×** | -7.0 | 9e-10 | 24/47 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.603×** | -6.3 | 6e-08 | 24/41 (NCI-H23, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.623×** | -5.9 | 6e-07 | 24/46 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.801×** | -3.9 | 0.010 | 15/42 (SK-MEL-2, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Captopril (drug)]] 5 µM |  | **0.752×** | -3.6 | 0.036 | 6/47 (HCT15, NCI-H460, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.763×** | -3.4 | 0.060 | 12/46 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trimetrexate (drug)]] 5 µM |  | 0.840× | -3.1 | 0.15 | 8/47 (H4, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.67 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.111× (z -9.1) |
| [[BT-474 (line)]] | alt | 9.36 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.125× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 7.82 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0861× (z -8.6) |
| [[HT-29 (line)]] | alt | 6.59 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.120× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0671× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 6.52 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.219× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 6.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -9.2) |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.209× (z -9.1) |
| [[A-427 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLAT]] | +0.71 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[PHB1]] | +0.70 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[BCS1L]] | +0.70 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[MRPL4]] | +0.70 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[HMBS]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ALKBH2]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[WDR18]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[STARD7]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[POLR3H]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[POLR1B]] | +0.65 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[IFRD2]] | +0.64 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[NKRF]] | +0.64 | +0.60 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM91]] | -0.58 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PNISR]] | -0.54 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[TSBP1-AS1]] | -0.54 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[DLEU2]] | -0.53 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[CD63]] | -0.53 | -0.49 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STEAP1]] | B | STEAP1 activity lowers RITA1's level | lines that do not express STEAP1 (11) vs lines expressing it (39) | 1.21× higher at baseline in the lines without STEAP1 | 0.078 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2 |
| [[LTBR]] | B | LTBR activity lowers RITA1's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.19× higher at baseline in the lines without LTBR | 0.081 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.716). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.4, -40.8); signed map (-10.6, -50.9). **Vector** length 52.4, 6.81% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.50 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.50 to 10); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +2.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +1.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.0 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +2.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -7.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | RBPJ interacting and tubulin associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:113,185,526-113,192,368 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14827, RITA; previously C12orf52 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96K30](https://www.uniprot.org/uniprotkb/Q96K30) (RBPJ-interacting and tubulin-associated protein 1):

> Tubulin-binding protein that acts as a negative regulator of Notch signaling pathway. Shuttles between the cytoplasm and the nucleus and mediates the nuclear export of RBPJ/RBPSUH, thereby preventing the interaction between RBPJ/RBPSUH and NICD product of Notch proteins (Notch intracellular domain), leading to down-regulate Notch-mediated transcription. May play a role in neurogenesis.

**Summary**, from NCBI Gene [84934](https://www.ncbi.nlm.nih.gov/gene/84934):

> Enables tubulin binding activity. Involved in negative regulation of Notch signaling pathway and nuclear export. Located in centrosome; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25925) · Entrez [84934](https://www.ncbi.nlm.nih.gov/gene/84934) · UniProt [Q96K30](https://www.uniprot.org/uniprotkb/Q96K30) · Ensembl [ENSG00000139405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139405)

## Data

Gene col 6302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6302); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6302]; `tensor/DDL_lfc|DDL_z.npy` [6302]; `embed/gene_vectors.npy` [6302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6302 or target_col == 6302). Every well: [[RITA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RITA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
