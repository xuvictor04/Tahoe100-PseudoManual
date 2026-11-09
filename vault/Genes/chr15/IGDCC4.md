---
symbol: "IGDCC4"
type: "gene"
col: 2394
ensembl_id: "ENSG00000103742"
name: "immunoglobulin superfamily DCC subclass member 4"
location: "15q22.31"
module: 13
arm: "+"
pooled_cpm: 2.97
n_lines_expressing: 32
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# IGDCC4

*immunoglobulin superfamily DCC subclass member 4* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.17× (z +14.9, q 0e+00, up in 7 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.666× (z -3.8, q 0.068, down in 10 of 26 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Clobetasol propionate (drug)]] 5 µM: 0.684× (z -3.5, q 0.068, down in 8 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H1792 0.0501×, SW480 0.185×, SW 900 0.0896×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H2347 0.255×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (NCI-H1792 0.108×; ⚠ cell-cycle shift, explains ~60% of this change); [[LJI308 (drug)]] 0.5 µM in 1 line (A-427 0.0449×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FMNL1-DT]] (+0.62, fdr 7e-06), [[LINC01226]] (+0.60, fdr 2e-05), [[MTMR9LP]] (+0.57, fdr 4e-05); moves opposite to [[SPIDR]] (-0.55, fdr 3e-05), [[TTLL5]] (-0.49, fdr 4e-05), [[PRELID2]] (-0.46, fdr 9e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FER1L6]] → it (grade B ⚠); 3 go from it, the strongest it → [[GRIK4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2394.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.17×** | +14.9 | 0e+00 | 7/18 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.35×** | +10.7 | 4e-24 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +8.9 | 1e-16 | 5/20 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +8.4 | 8e-15 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +7.0 | 3e-10 | 4/23 (HOP62, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +7.0 | 3e-10 | 1/7 (A549) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +6.1 | 8e-08 | 9/22 (HOP62, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.3 | 1e-05 | 8/27 (HOP62, SHP-77, …) | two highest doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +3.9 | 0.005 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.33×** | +3.7 | 0.014 | 2/27 (LoVo, A-427) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.019 | 3/26 (SW480, A549, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.020 | 1/16 (SNU-423) | inconsistent across doses | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.020 | 4/15 (RPMI-7951, NCI-H2030, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.040 | 3/24 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.1 | 0.063 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.064 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.071 | 1/18 (A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.076 | 3/16 (SW480, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2394.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H1792 0.0501×, SW480 0.185×, SW 900 0.0896×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H2347 0.255×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (NCI-H1792 0.108×; ⚠ cell-cycle shift, explains ~60% of this change); [[LJI308 (drug)]] 0.5 µM in 1 line (A-427 0.0449×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.666×** | -3.8 | 0.068 | 10/26 (RPMI-7951, SW 900, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.678×** | -3.6 | 0.068 | 10/25 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.684×** | -3.5 | 0.068 | 8/27 (SNU-423, NCI-H1792, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.685×** | -3.5 | 0.068 | 8/26 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.680× | -3.3 | 0.11 | 4/26 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.721× | -3.0 | 0.23 | 7/27 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0501× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 6.62 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 6.32 | 0 | 1 | — | [[LJI308 (drug)]] 0.5 µM 0.0449× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 4.74 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0366× (z -9.3) ⚠ cell-cycle shift, explains ~65% of this change |
| [[NCI-H2347 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 9.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0896× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.841 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.724 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.753 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.585 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.785 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.513 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FMNL1-DT]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[LINC01226]] | +0.60 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[MTMR9LP]] | +0.57 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[PIK3CD]] | +0.55 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[POU2F2]] | +0.52 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[MDGA1]] | +0.52 | +0.45 / +0.51 | both halves | 3e-05 | same gene group |
| [[NTNG2]] | +0.51 | +0.46 / +0.47 | both halves | 2e-05 | STRING 430 |
| [[APBB1]] | +0.51 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[SCAT1]] | +0.51 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[KCNIP1]] | +0.51 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[RERGL]] | +0.51 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[MYH16]] | +0.51 | +0.41 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPIDR]] | -0.55 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[TTLL5]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[PRELID2]] | -0.46 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[BCKDHB]] | -0.46 | -0.43 / -0.32 | both halves | 1e-04 |  |
| [[ARMC8]] | -0.45 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[SLF1]] | -0.45 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[BARD1]] | -0.45 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[RALGAPA2]] | -0.44 | -0.45 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FER1L6]] | B | FER1L6 activity lowers IGDCC4's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 2.02× higher at baseline in the lines without FER1L6 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[LINC01828]] | B | LINC01828 activity lowers IGDCC4's level | lines that do not express LINC01828 (17) vs lines expressing it (33) | 1.16× higher at baseline in the lines without LINC01828 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, ENSG00000230647, ENSG00000253891; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIK4]] | B | IGDCC4 activity raises GRIK4's level | lines that do not express IGDCC4 (18) vs lines expressing it (32) | 1.74× lower at baseline in the lines without IGDCC4 | 0.059 | ⚠ within organs, on part of the lines; also absent: C19orf18, ENSG00000176593, LINC02813; maybe low, not absent |
| [[PIK3CD]] | B | IGDCC4 activity raises PIK3CD's level | lines that do not express IGDCC4 (18) vs lines expressing it (32) | 2.15× lower at baseline in the lines without IGDCC4 | 0.073 | ⚠ within organs, on part of the lines; also absent: C19orf18, ENSG00000176593, LINC02813; maybe low, not absent |
| [[MTMR9LP]] | B | IGDCC4 activity raises MTMR9LP's level | lines that do not express IGDCC4 (18) vs lines expressing it (32) | 1.36× lower at baseline in the lines without IGDCC4 | 0.099 | ⚠ within organs, on part of the lines; also absent: C19orf18, ENSG00000176593, LINC02813; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.327). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.8, 37.1); signed map (35.9, 19.3). **Vector** length 45.2, 7.91% of its response variance represented; |z| ≥ 3 in 674 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +3.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -1.7 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -1.7 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | immunoglobulin superfamily DCC subclass member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:65,381,484-65,422,947 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NOPE, LOC57722 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing |
| Matched by | ensembl_id |

UniProt [Q8TDY8](https://www.uniprot.org/uniprotkb/Q8TDY8) carries no function annotation.

**Summary**, from NCBI Gene [57722](https://www.ncbi.nlm.nih.gov/gene/57722):

> Predicted to be involved in cell-cell adhesion. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13770](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13770) · Entrez [57722](https://www.ncbi.nlm.nih.gov/gene/57722) · UniProt [Q8TDY8](https://www.uniprot.org/uniprotkb/Q8TDY8) · Ensembl [ENSG00000103742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103742)

## Data

Gene col 2394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2394); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2394]; `tensor/DDL_lfc|DDL_z.npy` [2394]; `embed/gene_vectors.npy` [2394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2394 or target_col == 2394). Every well: [[IGDCC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGDCC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
