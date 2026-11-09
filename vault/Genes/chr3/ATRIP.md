---
symbol: "ATRIP"
type: "gene"
col: 8847
ensembl_id: "ENSG00000164053"
name: "ATR interacting protein"
location: "3p21.31"
module: 32
arm: "+"
pooled_cpm: 10.08
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# ATRIP

*ATR interacting protein* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.35× (z +19.9, q 0e+00, up in 37 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.768× (z -4.3, q 0.008, down in 15 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRF7]] (+0.66, fdr 7e-06), [[DHX58]] (+0.65, fdr 8e-06), [[DDX60]] (+0.64, fdr 1e-05); moves opposite to [[PRXL2A]] (-0.55, fdr 3e-05), [[NDRG3]] (-0.55, fdr 1e-05), [[POLR2B]] (-0.55, fdr 5e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +19.9 | 0e+00 | 37/43 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +12.4 | 6e-33 | 30/45 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.07×** | +11.9 | 1e-30 | 37/47 (SW480, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +10.2 | 4e-22 | 27/45 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +9.6 | 6e-20 | 24/43 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +9.2 | 4e-18 | 31/45 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.73×** | +8.7 | 3e-16 | 26/44 (NCI-H460, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +8.4 | 2e-15 | 28/46 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.63×** | +8.1 | 4e-14 | 30/47 (SW480, SW1417, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +8.0 | 5e-14 | 19/37 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +7.9 | 2e-13 | 27/48 (HOP62, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.57×** | +7.4 | 5e-12 | 25/47 (SW480, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.41×** | +5.6 | 8e-07 | 17/47 (SW480, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.39×** | +5.5 | 2e-06 | 17/40 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +4.6 | 2e-04 | 12/46 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.009 | 4/44 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.026 | 2/44 (Hs 766T, MIA PaCa-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.026 | 1/48 (RPMI-7951) | two highest doses | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.066 | 1/46 (HEC-1-A) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.14× | +3.0 | 0.066 | 4/48 (J82, NCI-H23, …) | top dose only |  |
| [[LJI308 (drug)]] 0.05 µM |  | **1.21×** | +2.9 | 0.081 | 3/45 (RPMI-7951, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8847.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.768×** | -4.3 | 0.008 | 15/46 (RKO, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.794×** | -3.8 | 0.045 | 14/45 (RPMI-7951, HS-578T, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.801×** | -3.6 | 0.052 | 6/47 (A498, HEC-1-A, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.814× | -3.4 | 0.10 | 13/44 (H4, C32, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.821× | -3.2 | 0.15 | 13/46 (NCI-H2030, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.825× | -3.1 | 0.15 | 7/44 (J82, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.827× | -3.1 | 0.15 | 8/44 (A549, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +9.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 8.89 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.103× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 7.71 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +13.9) | — |
| [[A498 (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +10.9) | — |
| [[A549 (line)]] | wt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 7.12 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 8.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.26× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 6.10 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0627× (z -8.5) |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0966× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +8.5) | — |
| [[LoVo (line)]] | wt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 5.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 8.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.8) | — |
| [[RKO (line)]] | wt | 8.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 17.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.105× (z -11.4) |
| [[SW 900 (line)]] | alt | 5.43 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0583× (z -10.1) |
| [[A-172 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRF7]] | +0.66 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[DHX58]] | +0.65 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[DDX60]] | +0.64 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[TRIM21]] | +0.64 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[TBCC]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[MAD2L1BP]] | +0.62 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[SIX1]] | +0.60 | +0.40 / +0.68 | both halves | 5e-05 |  |
| [[TAP1]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[DDX60L]] | +0.59 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[OASL]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[IFIT3]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[RIGI]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRXL2A]] | -0.55 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[NDRG3]] | -0.55 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[POLR2B]] | -0.55 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[OPA1]] | -0.55 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[TTC14]] | -0.54 | -0.32 / -0.61 | both halves | 2e-04 |  |
| [[AGO1]] | -0.54 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[TOMM20]] | -0.54 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[AP2A2]] | -0.53 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CNIH1]] | -0.53 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[VOPP1]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[RAB4A]] | -0.51 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[RTN3]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATRIP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IFIT3]] | B | IFIT3 activity lowers ATRIP's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 1.22× higher at baseline in the lines without IFIT3 | 0.087 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.0, 55.9); signed map (62.5, 34.2). **Vector** length 69.6, 11.6% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.53 to 23); *Interferon alpha/beta signaling* (reactome, mean cos +0.50 to 27); *IFIT antiviral response* (reactome, mean cos +0.55 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +19.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.0 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +7.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.5 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.2 | +0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.9 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | +0.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -1.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ATR interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,446,710-48,467,645 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12343, MGC20625, MGC21482, MGC26740 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Reactome | 22 pathways, smallest: Impaired BRCA2 binding to RAD51; Activation of ATR in response to replication stress; Fanconi Anemia Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXE1](https://www.uniprot.org/uniprotkb/Q8WXE1) (ATR-interacting protein):

> Required for checkpoint signaling after DNA damage. Required for ATR expression, possibly by stabilizing the protein.

**Summary**, from NCBI Gene [84126](https://www.ncbi.nlm.nih.gov/gene/84126):

> This gene encodes an essential component of the DNA damage checkpoint. The encoded protein binds to single-stranded DNA coated with replication protein A. The protein also interacts with the ataxia telangiectasia and Rad3 related protein kinase, resulting in its accumulation at intranuclear foci induced by DNA damage. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:33499](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33499) · Entrez [84126](https://www.ncbi.nlm.nih.gov/gene/84126) · UniProt [Q8WXE1](https://www.uniprot.org/uniprotkb/Q8WXE1) · Ensembl [ENSG00000164053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164053)

## Data

Gene col 8847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8847); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8847]; `tensor/DDL_lfc|DDL_z.npy` [8847]; `embed/gene_vectors.npy` [8847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8847 or target_col == 8847). Every well: [[ATRIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATRIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
