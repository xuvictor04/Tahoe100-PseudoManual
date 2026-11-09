---
symbol: "EFCAB8"
type: "gene"
col: 13267
ensembl_id: "ENSG00000215529"
name: "EF-hand calcium binding domain 8"
location: "20q11.21"
module: 39
arm: "+"
pooled_cpm: 5.64
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# EFCAB8

*EF-hand calcium binding domain 8* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.66× (z +20.7, q 0e+00, up in 35 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.419× (z -8.3, q 5e-14, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01588]] (+0.79, fdr 7e-06), [[SMIM15-AS1]] (+0.78, fdr 7e-06), [[NUP210L]] (+0.77, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FLJ12825]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13267.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.66×** | +20.7 | 0e+00 | 35/38 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.96×** | +14.7 | 0e+00 | 3/7 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.21×** | +12.7 | 2e-34 | 10/14 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +9.7 | 3e-20 | 16/23 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +8.8 | 1e-16 | 25/39 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.51×** | +8.8 | 2e-16 | 29/46 (SW480, HT-29, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **2.20×** | +7.5 | 5e-12 | 29/46 (LoVo, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.19×** | +6.5 | 5e-09 | 27/45 (A-427, A498, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +5.8 | 4e-07 | 17/37 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.73×** | +5.2 | 1e-05 | 18/46 (J82, Hs 766T, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +4.9 | 5e-05 | 3/8 (J82, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **2.25×** | +4.0 | 0.002 | 7/46 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.0 | 0.003 | 6/47 (PANC-1, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.007 | 11/46 (SW480, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.013 | 9/36 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.034 | 10/42 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Nevirapine (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.072 | 4/45 (NCI-H2030, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13267.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.419×** | -8.3 | 5e-14 | 28/46 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.458×** | -7.5 | 2e-11 | 23/38 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.331×** | -5.5 | 6e-06 | 19/32 (HOP62, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.620×** | -4.6 | 7e-04 | 18/45 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.606×** | -4.2 | 0.003 | 19/43 (NCI-H23, SW48, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.741×** | -4.1 | 0.005 | 17/46 (NCI-H1792, NCI-H2030, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.472×** | -3.8 | 0.014 | 12/44 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.684×** | -3.6 | 0.018 | 17/45 (SW1417, PANC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.766×** | -3.6 | 0.018 | 11/47 (NCI-H661, hTERT-HPNE, …) | top dose only |  |
| [[Radotinib (drug)]] 0.5 µM |  | **0.701×** | -3.4 | 0.034 | 9/40 (SW 900, LS 180, …) | rises with dose |  |
| [[Ritonavir (drug)]] 0.5 µM |  | **0.701×** | -3.4 | 0.034 | 10/42 (SW 900, SW48, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.703×** | -3.4 | 0.034 | 18/45 (SW1417, PANC-1, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.519×** | -3.3 | 0.044 | 7/30 (KATO III, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.711×** | -3.3 | 0.044 | 13/39 (HOP62, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.727×** | -3.1 | 0.085 | 6/46 (SW 1271, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 21.9 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +9.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.134× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[PANC-1 (line)]] | alt | 15.0 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -12.0) |
| [[SW480 (line)]] | alt | 5.00 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.129× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -9.1) |
| [[BT-474 (line)]] | alt | 8.30 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0465× (z -10.8) |
| [[J82 (line)]] | alt | 6.58 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +9.0) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.116× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 2.17 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.51× (z +11.0) | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0843× (z -10.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 2.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.83× (z +9.0) | — |
| [[A498 (line)]] | wt | 1.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 6.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.79× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 3.99 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.1× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 6.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.02× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 4.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +8.6) | — |
| [[KATO III (line)]] | alt | 5.43 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0442× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 2.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 3.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 3.71 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0767× (z -8.5) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01588]] | +0.79 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.78 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.77 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.74 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[SLC2A9]] | +0.74 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.73 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[MYH3]] | +0.72 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[MSH4]] | +0.72 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[BAAT]] | +0.72 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[PARD6G-AS1]] | +0.72 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[MPP4]] | +0.72 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[SPOCK2]] | +0.72 | +0.59 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLJ12825]] | B | FLJ12825 activity raises EFCAB8's level | lines that do not express FLJ12825 (15) vs lines expressing it (35) | 1.66× lower at baseline in the lines without FLJ12825 | 0.085 | ⚠ within organs, on part of the lines; also absent: HOXC10, HOXC6, HOXC8; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.782). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.5, -12.8); signed map (17.1, 6.0). **Vector** length 82.7, 15.2% of its response variance represented; |z| ≥ 3 in 1,292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.2 | +12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +14.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +20.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +7.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +6.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.4 | -3.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.1 | -5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.9 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -8.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -7.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.3 | -4.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | EF-hand calcium binding domain 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:32,858,923-32,961,845 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

UniProt [A8MWE9](https://www.uniprot.org/uniprotkb/A8MWE9) carries no function annotation.

**Summary**, from NCBI Gene [388795](https://www.ncbi.nlm.nih.gov/gene/388795):

> Predicted to enable calcium ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34532](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34532) · Entrez [388795](https://www.ncbi.nlm.nih.gov/gene/388795) · UniProt [A8MWE9](https://www.uniprot.org/uniprotkb/A8MWE9) · Ensembl [ENSG00000215529](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215529)

## Data

Gene col 13267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13267); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13267]; `tensor/DDL_lfc|DDL_z.npy` [13267]; `embed/gene_vectors.npy` [13267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13267 or target_col == 13267). Every well: [[EFCAB8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFCAB8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
