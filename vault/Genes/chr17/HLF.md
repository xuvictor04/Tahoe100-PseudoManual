---
symbol: "HLF"
type: "gene"
col: 3009
ensembl_id: "ENSG00000108924"
name: "HLF transcription factor, PAR bZIP family member"
location: "17q22"
module: 14
arm: "+"
pooled_cpm: 4.12
n_lines_expressing: 31
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# HLF

*HLF transcription factor, PAR bZIP family member* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 19.0× (z +35.7, q 0e+00, up in 15 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.160×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HepG2/C3A 0.159×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.144×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.251×); [[Auranofin (drug)]] 5 µM in 1 line (HepG2/C3A 0.266×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC148]] (+0.58, fdr 1e-05), [[KCNN2]] (+0.57, fdr 1e-05), [[SYNPO]] (+0.54, fdr 3e-05); moves opposite to [[SENP5]] (-0.55, fdr 5e-05), [[TMEM11-DT]] (-0.53, fdr 1e-04), [[SNHG30]] (-0.52, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[FBXW11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3009.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **19.0×** | +35.7 | 0e+00 | 15/16 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **14.4×** | +22.0 | 0e+00 | 20/21 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **4.88×** | +19.2 | 0e+00 | 23/24 (SW480, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.91×** | +17.7 | 0e+00 | 15/16 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.57×** | +14.2 | 2e-43 | 2/3 (SNU-423, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.81×** | +13.5 | 2e-39 | 3/5 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.71×** | +13.3 | 2e-38 | 22/26 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.46×** | +12.8 | 9e-36 | 20/24 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.95×** | +12.7 | 4e-35 | 1/3 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.34×** | +12.6 | 2e-34 | 18/24 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.33×** | +10.3 | 3e-23 | 17/25 (SNU-423, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.74×** | +8.6 | 3e-16 | 13/19 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.54×** | +8.0 | 7e-14 | 18/26 (SHP-77, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.24×** | +6.9 | 2e-10 | 12/22 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.0 | 3e-05 | 1/15 (BT-474) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.60×** | +4.3 | 6e-04 | 6/16 (SNU-423, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.001 | 3/25 (NCI-H23, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.64×** | +3.9 | 0.003 | 3/13 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3009.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.160×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HepG2/C3A 0.159×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.144×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.251×); [[Auranofin (drug)]] 5 µM in 1 line (HepG2/C3A 0.266×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Malotilate (drug)]] 0.5 µM |  | 0.678× | -3.3 | 0.26 | 4/21 (HOP62, HepG2/C3A, …) | two highest doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.672× | -3.3 | 0.26 | 2/25 (NCI-H1792, KATO III) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.690× | -3.2 | 0.26 | 5/22 (HepG2/C3A, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | 0.686× | -3.0 | 0.30 | 4/26 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Megestrol (drug)]] 5 µM |  | 0.782× | -3.0 | 0.30 | 11/26 (HT-29, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3009. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 219 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -20.1) |
| [[NCI-H460 (line)]] | wt | 1.45 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.9× (z +14.7) | — |
| [[HEC-1-A (line)]] | alt | 2.30 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.7× (z +15.9) | — |
| [[A-172 (line)]] | wt | 1.76 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 69.8× (z +13.7) | — |
| [[HOP62 (line)]] | alt | 1.16 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 53.8× (z +11.9) | — |
| [[LoVo (line)]] | wt | 1.48 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 2.03 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.8× (z +13.2) | — |
| [[SW480 (line)]] | alt | 1.03 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +10.4) | — |
| [[A549 (line)]] | wt | 1.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.8× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 2.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 1.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 2.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 2.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +11.8) | — |
| [[A-427 (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.746 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.711 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.700 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3009), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC148]] | +0.58 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[KCNN2]] | +0.57 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.54 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[REPIN1]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TEF]] | +0.53 | +0.53 / +0.53 | both halves | 1e-05 | same gene group |
| [[DYNLRB2-AS1]] | +0.53 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[RHOU]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[LIMA1]] | +0.52 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[TCEANC]] | +0.52 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ZNF608]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[NUAK2]] | +0.51 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ZNF620]] | +0.51 | +0.52 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP5]] | -0.55 | -0.40 / -0.67 | both halves | 5e-05 |  |
| [[TMEM11-DT]] | -0.53 | -0.34 / -0.65 | both halves | 1e-04 |  |
| [[SNHG30]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[PPHLN1]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[TNPO3]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[NAP1L4]] | -0.49 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[MFN1]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[GUCD1]] | -0.49 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[SAP30L-AS1]] | -0.49 | -0.17 / -0.60 | ⚠ one half (not replicated) | 0.001 |  |
| [[UFD1]] | -0.48 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[SMG1P5]] | -0.48 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[COP1]] | -0.48 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ZFC3H1]] | -0.48 | -0.39 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXW11]] | B | HLF activity lowers FBXW11's level | lines that do not express HLF (19) vs lines expressing it (31) | 1.12× higher at baseline in the lines without HLF | 0.039 | ⚠ within organs, on part of the lines; also absent: FAM230C, CHST8, GPR158; maybe low, not absent |
| [[PLCB4]] | B | HLF activity raises PLCB4's level | lines that do not express HLF (19) vs lines expressing it (31) | 1.96× lower at baseline in the lines without HLF | 0.060 | ⚠ within organs, on part of the lines; also absent: FAM230C, CHST8, GPR158; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.451). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.3, 33.9); signed map (49.1, 9.6). **Vector** length 46.2, 8.38% of its response variance represented; |z| ≥ 3 in 719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +22.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +19.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +17.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +35.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +12.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +6.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.8 | +2.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.3 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.2 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | +1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.7 | +0.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | -0.6 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | HLF transcription factor, PAR bZIP family member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:55,264,960-55,325,187 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33822 |
| Gene groups (HGNC) | PAR bZIP family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16534](https://www.uniprot.org/uniprotkb/Q16534) (Transcription factor HLF):

> Transcription factor which selectively binds with high affinity to the consensus sequence 5'-GTTACGTAAT-3' and to closely related sites. Has transcriptional activator activity. Also has transcriptional repressor activity (By similarity). Binds to multiple sites in the promoter regions of coagulation factors F8 and F9 and activates transcription; transactivation activity is enhanced by formation of a heterodimer with DBP. Binds to the promoter region of IRF2 and activates transcription (By …

**Summary**, from NCBI Gene [3131](https://www.ncbi.nlm.nih.gov/gene/3131):

> This gene encodes a member of the proline and acidic-rich (PAR) protein family, a subset of the bZIP transcription factors. The encoded protein forms homodimers or heterodimers with other PAR family members and binds sequence-specific promoter elements to activate transcription. Chromosomal translocations fusing portions of this gene with the E2A gene cause a subset of childhood B-lineage acute lymphoid leukemias. Alternatively spliced transcript variants have been described, but their …

**Accessions** — [HGNC:4977](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4977) · Entrez [3131](https://www.ncbi.nlm.nih.gov/gene/3131) · UniProt [Q16534](https://www.uniprot.org/uniprotkb/Q16534) · Ensembl [ENSG00000108924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108924)

## Data

Gene col 3009: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3009); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3009, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3009]; `tensor/DDL_lfc|DDL_z.npy` [3009]; `embed/gene_vectors.npy` [3009]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3009 or target_col == 3009). Every well: [[HLF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
