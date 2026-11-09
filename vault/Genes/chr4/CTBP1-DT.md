---
symbol: "CTBP1-DT"
type: "gene"
col: 12286
ensembl_id: "ENSG00000196810"
name: "CTBP1 divergent transcript"
location: "4p16.3"
module: 10
arm: "+"
pooled_cpm: 6.34
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CTBP1-DT

*CTBP1 divergent transcript* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +12.2, q 2e-31, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.306× (z -12.4, q 1e-32, down in 32 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.326× (z -11.8, q 2e-29, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00667]] (+0.77, fdr 7e-06), [[MZF1-AS1]] (+0.75, fdr 5e-05), [[TASOR]] (+0.75, fdr 2e-05); moves opposite to [[FAM118A]] (-0.72, fdr 1e-05), [[DPY30]] (-0.66, fdr 6e-05), [[KYAT1]] (-0.64, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ANKRD18B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12286.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +12.2 | 2e-31 | 39/42 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +8.3 | 4e-14 | 12/17 (LS 180, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +7.1 | 3e-10 | 8/10 (BT-474, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.7 | 4e-09 | 16/27 (NCI-H460, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.7 | 3e-04 | 17/39 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.003 | 11/47 (SW480, A498, …) | top dose only | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.075 | 7/47 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.2 | 0.096 | 8/33 (HOP62, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 1.76× | +3.1 | 0.12 | 7/44 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.23× | +3.1 | 0.12 | 9/46 (HCT15, RKO, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12286.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.306×** | -12.4 | 1e-32 | 32/42 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.326×** | -11.8 | 2e-29 | 40/47 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.373×** | -10.4 | 7e-23 | 31/46 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.376×** | -10.3 | 1e-22 | 35/46 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.449×** | -8.4 | 5e-15 | 33/47 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.506×** | -7.2 | 8e-11 | 30/47 (J82, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.506×** | -7.1 | 8e-11 | 27/45 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.540×** | -6.5 | 7e-09 | 26/46 (LS 180, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.578×** | -5.4 | 3e-06 | 24/43 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.529×** | -5.4 | 3e-06 | 20/47 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.668×** | -4.2 | 0.001 | 15/47 (MIA PaCa-2, J82, …) | two highest doses | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.716×** | -3.5 | 0.021 | 13/47 (KATO III, C-33 A, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.718×** | -3.5 | 0.022 | 12/45 (SK-MEL-2, LS 180, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.571×** | -3.1 | 0.084 | 10/36 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12286. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 8.41 | 0 | 3 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0806× (z -11.7) |
| [[A-427 (line)]] | wt | 8.83 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.124× (z -9.6) |
| [[BT-474 (line)]] | alt | 9.07 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0864× (z -10.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 5.98 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0648× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -9.3) |
| [[HT-29 (line)]] | alt | 4.18 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0586× (z -10.3) |
| [[J82 (line)]] | alt | 12.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.216× (z -8.8) |
| [[LoVo (line)]] | wt | 6.52 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0401× (z -15.6) |
| [[NCI-H460 (line)]] | wt | 4.86 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.143× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 5.89 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -10.8) |
| [[A-172 (line)]] | wt | 6.83 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 8.39 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0800× (z -11.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 8.04 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 5.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 3.58 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM 0.0573× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 5.48 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0883× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 4.67 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0458× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -9.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 5.48 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -9.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12286), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00667]] | +0.77 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[MZF1-AS1]] | +0.75 | +0.76 / +0.40 | both halves | 5e-05 |  |
| [[TASOR]] | +0.75 | +0.81 / +0.48 | both halves | 2e-05 |  |
| [[ZNF747]] | +0.74 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[ZC3H4]] | +0.74 | +0.79 / +0.42 | both halves | 4e-05 |  |
| [[LEKR1]] | +0.72 | +0.73 / +0.43 | both halves | 3e-05 |  |
| [[PSMG3-AS1]] | +0.72 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[CCT6B]] | +0.71 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | +0.71 | +0.69 / +0.49 | both halves | 1e-05 | same gene group |
| [[SEPTIN7-DT]] | +0.71 | +0.66 / +0.45 | both halves | 3e-05 | same gene group |
| [[MAD2L1-DT]] | +0.70 | +0.66 / +0.39 | both halves | 5e-05 | same gene group |
| [[CLHC1]] | +0.70 | +0.67 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.72 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[DPY30]] | -0.66 | -0.65 / -0.38 | both halves | 6e-05 |  |
| [[KYAT1]] | -0.64 | -0.66 / -0.34 | both halves | 1e-04 |  |
| [[CBFA2T2]] | -0.63 | -0.70 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD18B]] | B | ANKRD18B activity raises CTBP1-DT's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.19× lower at baseline in the lines without ANKRD18B | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[TOP2A]] | B | TOP2A activity lowers CTBP1-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC00886]] | B | LINC00886 activity raises CTBP1-DT's level | lines that do not express LINC00886 (16) vs lines expressing it (34) | 1.31× lower at baseline in the lines without LINC00886 | 0.038 | ⚠ within organs, on part of the lines; also absent: RASEF; maybe low, not absent |
| [[FRG1-DT]] | B | FRG1-DT activity raises CTBP1-DT's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 1.37× lower at baseline in the lines without FRG1-DT | 0.043 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent |
| [[ANKRD18B]] | B | ANKRD18B activity strengthens CTBP1-DT's drug response | lines that do not express ANKRD18B (22) vs lines expressing it (25) | the lines without ANKRD18B respond 0.93× as strongly (z diff +0.45); strongest at Digitoxin 5 µM: 0.36x vs 0.24x (z diff +2.1) | 0.054 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2; target measured in part of the lines; both ways; artifact flags |
| [[RIMS2]] | B | RIMS2 activity raises CTBP1-DT's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 1.20× lower at baseline in the lines without RIMS2 | 0.073 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[TOP2B]] | B | TOP2B activity lowers CTBP1-DT's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.782). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.5, 13.6); signed map (28.0, -13.0). **Vector** length 73.0, 12.6% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +8.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +3.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -6.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.8 | -7.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -10.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | -11.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -7.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | CTBP1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4p16.3 — chr4:1,248,877-1,288,856 (+) |
| Ensembl biotype | lncRNA |
| Also known as | DDUP, MGC21675; previously C4orf42, CTBP1-AS1, CTBP1-AS2 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

**Function**, from UniProt [C0HM98](https://www.uniprot.org/uniprotkb/C0HM98) (DNA damage up-regulated protein):

> Promotes DNA damage repair through both homologous recombination repair (HRR) and post-replication repair (PRR) mechanisms. Enhances the retention of DNA damage response protein RAD18 at sites of DNA damage. This allows for HRR via association of RAD18 with RAD51C and for PRR via RAD18-mediated promotion of PCNA monoubiquitination.

**Summary**, from NCBI Gene [92070](https://www.ncbi.nlm.nih.gov/gene/92070):

> Involved in DNA damage tolerance and recombinational repair. Located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28307) · Entrez [92070](https://www.ncbi.nlm.nih.gov/gene/92070) · UniProt [C0HM98](https://www.uniprot.org/uniprotkb/C0HM98) · Ensembl [ENSG00000196810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196810)

## Data

Gene col 12286: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12286); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12286, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12286]; `tensor/DDL_lfc|DDL_z.npy` [12286]; `embed/gene_vectors.npy` [12286]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12286 or target_col == 12286). Every well: [[CTBP1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTBP1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
