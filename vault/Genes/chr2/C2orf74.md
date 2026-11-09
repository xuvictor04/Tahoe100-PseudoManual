---
symbol: "C2orf74"
type: "gene"
col: 14146
ensembl_id: "ENSG00000237651"
name: "DPM1 ER membrane anchor 1"
location: "2p15"
module: 12
arm: "+"
pooled_cpm: 8.85
n_lines_expressing: 37
n_dd_up: 13
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 74
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# C2orf74

*DPM1 ER membrane anchor 1* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.76× (z +8.7, q 2e-15, up in 27 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.246× (z -15.2, q 0e+00, down in 32 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2orf74-DT]] (+0.68, fdr 7e-06, ⚠ same locus), [[ZNF737]] (+0.66, fdr 7e-06), [[STK16]] (+0.61, fdr 7e-06), [[CCDC43]] (+0.61, fdr 1e-05); moves opposite to [[GPC4]] (-0.59, fdr 1e-05), [[TSPAN3]] (-0.55, fdr 2e-05), [[PRPS2]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C2orf74-DT]] → it (grade C ⚠); 74 go from it, the strongest it → cells under [[Dihydroartemisinin (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14146.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +8.7 | 2e-15 | 27/34 (A-172, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +4.6 | 0.001 | 11/27 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.5 | 0.001 | 12/27 (AsPC-1, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.1 | 0.005 | 8/16 (SW 900, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.008 | 13/34 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.010 | 11/34 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.016 | 13/34 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.6 | 0.020 | 9/34 (NCI-H23, hTERT-HPNE, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +3.4 | 0.043 | 9/34 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.4 | 0.043 | 9/26 (A-172, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.050 | 5/32 (NCI-H23, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.050 | 5/33 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.060 | 8/31 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14146.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.246×** | -15.2 | 0e+00 | 32/34 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.282×** | -13.7 | 3e-40 | 33/34 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.346×** | -11.5 | 3e-28 | 30/34 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.348×** | -11.4 | 5e-28 | 28/32 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.478×** | -8.0 | 2e-13 | 26/34 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.508×** | -7.3 | 3e-11 | 21/33 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -6.3 | 2e-08 | 21/33 (NCI-H23, Hs 766T, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.576×** | -6.0 | 2e-07 | 21/34 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.391×** | -5.3 | 7e-06 | 21/31 (A-172, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.410×** | -5.0 | 3e-05 | 18/34 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.632×** | -4.9 | 4e-05 | 20/34 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[EX229 (drug)]] 5 µM |  | **0.425×** | -4.8 | 6e-05 | 15/32 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.670×** | -4.3 | 7e-04 | 17/34 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.661×** | -4.3 | 7e-04 | 15/28 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.689×** | -4.0 | 0.002 | 10/31 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.702×** | -3.6 | 0.010 | 15/33 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Gefitinib (drug)]] 5 µM |  | **0.743×** | -3.2 | 0.042 | 7/34 (NCI-H460, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0729× (z -17.5) |
| [[A-172 (line)]] | wt | 17.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.247× (z -9.0) |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0817× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 12.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.173× (z -10.5) |
| [[A-427 (line)]] | wt | 15.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.132× (z -10.7) |
| [[HOP62 (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0730× (z -13.4) |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 17.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -8.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -8.5) |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -9.8) |
| [[A549 (line)]] | wt | 9.73 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -10.6) |
| [[Hs 766T (line)]] | wt | 9.88 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.143× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 5.51 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0654× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.121× (z -9.5) |
| [[A498 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.911 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.937 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.906 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2orf74-DT]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[ZNF737]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[STK16]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[CCDC43]] | +0.61 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[TRMT10B]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PEX12]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[SNHG11]] | +0.59 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[DUSP15]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[EBAG9]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[BCAS2]] | +0.59 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[NFKBIL1]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ZNF727]] | +0.58 | +0.43 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPC4]] | -0.59 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TSPAN3]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[PRPS2]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[STT3B]] | -0.53 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[TBC1D4]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ADAM15]] | -0.51 | -0.39 / -0.62 | both halves | 6e-05 |  |
| [[PKP4]] | -0.51 | -0.47 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2orf74-DT]] | C | C2orf74-DT activity raises C2orf74's level | lines that do not express C2orf74-DT (15) vs lines expressing it (35) | 4.72× lower at baseline in the lines without C2orf74-DT | 0.060 | ⚠ within organs, on part of the lines; also absent: C2orf74, NR3C1, FIGN; co-absent with the target; its own permutation p |

### Downstream of this gene

*74 arrows, 74 of them with an alert ⚠; grade A 0, B 0, C 74. Shown: the 12 strongest; 62 more arrows (62 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Dihydroartemisinin (drug)]] 5 µM | C | C2orf74 activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.36× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| cells under [[Erlotinib (drug)]] 0.05 µM | C | C2orf74 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.27× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| cells under [[Fenofibrate (drug)]] 0.05 µM | C | C2orf74 activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.29× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| cells under [[Glasdegib (drug)]] 5 µM | C | C2orf74 activity lowers the cells' numbers under Glasdegib 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.23× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1; cell counts less trustworthy |
| cells under [[Erdafitinib (drug)]] 5 µM | C | C2orf74 activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.18× the cells of the other lines | 0.011 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| cells under [[AZD2858 (drug)]] 5 µM | C | C2orf74 activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.36× the cells of the other lines | 0.012 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| cells under [[Sulfatinib (drug)]] 0.5 µM | C | C2orf74 activity lowers the cells' numbers under Sulfatinib 0.5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.22× the cells of the other lines | 0.012 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| cells under [[Almonertinib (hydrochloride) (drug)]] 0.5 µM | C | C2orf74 activity raises the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (protects the cells) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 0.84× the cells of the other lines | 0.015 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| cells under [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM | C | C2orf74 activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.26× the cells of the other lines | 0.018 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| cells under [[Penfluridol (drug)]] 5 µM | C | C2orf74 activity lowers the cells' numbers under Penfluridol 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.20× the cells of the other lines | 0.019 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| cells under [[Furosemide (drug)]] 0.5 µM | C | C2orf74 activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.19× the cells of the other lines | 0.019 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| cells under [[Lopinavir (drug)]] 5 µM | C | C2orf74 activity lowers the cells' numbers under Lopinavir 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.19× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-33.5, 21.5); signed map (-3.7, -18.2). **Vector** length 63.7, 13.5% of its response variance represented; |z| ≥ 3 in 700 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.5 | +8.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.1 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | -2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -13.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -15.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.4 | -8.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | DPM1 ER membrane anchor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:61,145,068-61,164,828 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOC339804; previously C2orf74 |
| Matched by | ensembl_id |

UniProt [A8MZ97](https://www.uniprot.org/uniprotkb/A8MZ97) carries no function annotation.

**Summary**, from NCBI Gene [339804](https://www.ncbi.nlm.nih.gov/gene/339804):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34439](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34439) · Entrez [339804](https://www.ncbi.nlm.nih.gov/gene/339804) · UniProt [A8MZ97](https://www.uniprot.org/uniprotkb/A8MZ97) · Ensembl [ENSG00000237651](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237651)

## Data

Gene col 14146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14146); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14146]; `tensor/DDL_lfc|DDL_z.npy` [14146]; `embed/gene_vectors.npy` [14146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14146 or target_col == 14146). Every well: [[C2orf74 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2orf74.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
