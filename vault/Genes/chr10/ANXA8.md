---
symbol: "ANXA8"
type: "gene"
col: 15452
ensembl_id: "ENSG00000265190"
name: "annexin A8"
location: "10q11.22"
module: 66
arm: "+"
pooled_cpm: 2.34
n_lines_expressing: 12
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# ANXA8

*annexin A8* — 10q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.70× (z +9.2, q 2e-17, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.21× (z +5.2, q 3e-05, up in 2 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Lumateperone (tosylate) (drug)]] 0.5 µM: 0.448× (z -3.8, q 0.071, down in 0 of 9 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYLK]] (+0.61, fdr 1e-05), [[SULF1]] (+0.60, fdr 3e-05), [[CFL2]] (+0.59, fdr 4e-05); moves opposite to [[SS18L1]] (-0.46, fdr 2e-04), [[QPCTL]] (-0.45, fdr 4e-04), [[SNX14]] (-0.43, fdr 1e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SULF1]] → it (grade C ⚠); 7 go from it, the strongest it → [[CYLD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.70×** | +9.2 | 2e-17 | 2/4 (HOP62, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.49×** | +8.0 | 4e-13 | 4/6 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.49×** | +7.4 | 3e-11 | 3/4 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +5.2 | 3e-05 | 2/9 (A549, SNU-423) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +5.2 | 3e-05 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.42×** | +5.0 | 7e-05 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +4.4 | 9e-04 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.64×** | +4.4 | 9e-04 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.83×** | +4.0 | 0.005 | 0/9 | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.28×** | +3.9 | 0.006 | 8/10 (HOP62, Hs 766T, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.14×** | +3.5 | 0.020 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.07×** | +3.4 | 0.029 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +3.4 | 0.029 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +3.3 | 0.038 | 0/7 | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **2.01×** | +3.2 | 0.045 | 0/6 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **2.00×** | +3.2 | 0.045 | 0/6 | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.62×** | +3.2 | 0.045 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.99×** | +3.1 | 0.066 | 6/9 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.43×** | +2.9 | 0.095 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15452.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | **0.448×** | -3.8 | 0.071 | 0/9 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 10.1 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 3.12× (z +10.8) ⚠ position not correctable | — |
| [[Hs 766T (line)]] | wt | 54.5 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.22× (z +9.1) ⚠ position not correctable | — |
| [[A-172 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.142 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.186 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.160 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.204 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.151 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.147 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.171 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.160 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.162 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.177 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.201 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.149 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.647 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLK]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[SULF1]] | +0.60 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[CFL2]] | +0.59 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[CHRDL1]] | +0.58 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[SYNPO]] | +0.57 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[MXRA5]] | +0.56 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[LINC00842]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[CCDC80]] | +0.54 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[COL12A1]] | +0.53 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[GFRA1]] | +0.53 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[LIMS2]] | +0.52 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[CAV1]] | +0.51 | +0.46 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SS18L1]] | -0.46 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[QPCTL]] | -0.45 | -0.26 / -0.54 | both halves | 4e-04 |  |
| [[SNX14]] | -0.43 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[SDF2]] | -0.42 | -0.29 / -0.42 | both halves | 3e-04 |  |
| [[ZNF549]] | -0.41 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[ARHGEF18]] | -0.41 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[RERE]] | -0.41 | -0.29 / -0.38 | both halves | 2e-04 |  |
| [[TMEM41A]] | -0.40 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[RNF168]] | -0.40 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[SDHAF1]] | -0.40 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[ESCO1]] | -0.40 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[PHC2]] | -0.40 | -0.30 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SULF1]] | C | SULF1 activity raises ANXA8's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 2.01× lower at baseline in the lines without SULF1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT; co-absent with the target |
| [[SHISAL1]] | C | SHISAL1 activity raises ANXA8's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 1.56× lower at baseline in the lines without SHISAL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[MXRA5]] | C | MXRA5 activity raises ANXA8's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 2.51× lower at baseline in the lines without MXRA5 | 0.042 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476; co-absent with the target |
| [[LINC00842]] | C | LINC00842 activity raises ANXA8's level | lines that do not express LINC00842 (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without LINC00842 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000276850, KRT81, EDN2; co-absent with the target |
| [[SIM1]] | C | SIM1 activity raises ANXA8's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.55× lower at baseline in the lines without SIM1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[POSTN]] | C | POSTN activity raises ANXA8's level | lines that do not express POSTN (38) vs lines expressing it (12) | 1.69× lower at baseline in the lines without POSTN | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYLD]] | B | ANXA8 activity raises CYLD's level | lines that do not express ANXA8 (38) vs lines expressing it (12) | 1.52× lower at baseline in the lines without ANXA8 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[RFTN1]] | B | ANXA8 activity raises RFTN1's level | lines that do not express ANXA8 (38) vs lines expressing it (12) | 2.72× lower at baseline in the lines without ANXA8 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[DPYSL3]] | B | ANXA8 activity raises DPYSL3's level | lines that do not express ANXA8 (38) vs lines expressing it (12) | 2.85× lower at baseline in the lines without ANXA8 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[CAV2]] | B | ANXA8 activity strengthens CAV2's drug response | lines that do not express ANXA8 (31) vs lines expressing it (9) | the lines without ANXA8 respond 0.62× as strongly (z diff +1.92); strongest at Panobinostat 5 µM: 0.58x vs 0.36x (z diff +3.9) | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; target measured in part of the lines; artifact flags |
| [[LINC00842]] | C | ANXA8 activity raises LINC00842's level | lines that do not express ANXA8 (38) vs lines expressing it (12) | 3.21× lower at baseline in the lines without ANXA8 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[MXRA5]] | C | ANXA8 activity raises MXRA5's level | lines that do not express ANXA8 (38) vs lines expressing it (12) | 4.77× lower at baseline in the lines without ANXA8 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[ABI3BP]] | C | ANXA8 activity raises ABI3BP's level | lines that do not express ANXA8 (38) vs lines expressing it (12) | 4.40× lower at baseline in the lines without ANXA8 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (57.9, 21.3); signed map (43.0, 21.0). **Vector** length 20.5, 4.99% of its response variance represented; |z| ≥ 3 in 183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.6 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.9 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | +1.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.8 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.5 | -0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.5 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.5 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -2.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.4 | -0.9 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -0.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | annexin A8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.22 — chr10:47,460,162-47,484,158 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ANX8 |
| Gene groups (HGNC) | Annexins |
| Matched by | ensembl_id |

**Function**, from UniProt [P13928](https://www.uniprot.org/uniprotkb/P13928) (Annexin A8):

> This protein is an anticoagulant protein that acts as an indirect inhibitor of the thromboplastin-specific complex, which is involved in the blood coagulation cascade.

**Summary**, from NCBI Gene [653145](https://www.ncbi.nlm.nih.gov/gene/653145):

> This gene encodes a member of the annexin family of evolutionarily conserved Ca2+ and phospholipid binding proteins. The encoded protein may function as an an anticoagulant that indirectly inhibits the thromboplastin-specific complex. Overexpression of this gene has been associated with acute myelocytic leukemia. A highly similar duplicated copy of this gene is found in close proximity on the long arm of chromosome 10. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:546) · Entrez [653145](https://www.ncbi.nlm.nih.gov/gene/653145) · UniProt [P13928](https://www.uniprot.org/uniprotkb/P13928) · Ensembl [ENSG00000265190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000265190)

## Data

Gene col 15452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15452); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15452]; `tensor/DDL_lfc|DDL_z.npy` [15452]; `embed/gene_vectors.npy` [15452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15452 or target_col == 15452). Every well: [[ANXA8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANXA8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
