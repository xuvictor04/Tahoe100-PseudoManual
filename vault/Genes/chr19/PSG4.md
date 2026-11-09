---
symbol: "PSG4"
type: "gene"
col: 14340
ensembl_id: "ENSG00000243137"
name: "pregnancy specific beta-1-glycoprotein 4"
location: "19q13.31"
module: 125
arm: "+"
pooled_cpm: 2.99
n_lines_expressing: 10
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 18
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# PSG4

*pregnancy specific beta-1-glycoprotein 4* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.81× (z +10.8, q 1e-24, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 3.00× (z +8.0, q 2e-13, up in 4 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSG9]] (+0.80, fdr 7e-06, ⚠ same locus), [[ANKRD30B]] (+0.69, fdr 1e-05), [[SLAMF7]] (+0.69, fdr 7e-06), [[NGF]] (+0.61, fdr 3e-05); moves opposite to [[ANGPTL4]] (-0.46, fdr 7e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[LINC00958]] → it (grade C ⚠); 18 go from it, the strongest it → [[ESR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.81×** | +10.8 | 1e-24 | 2/3 (J82, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.45×** | +8.8 | 5e-16 | 4/6 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.00×** | +8.0 | 2e-13 | 4/7 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.71×** | +7.4 | 2e-11 | 2/3 (J82, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.67×** | +7.2 | 8e-11 | 4/7 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.33×** | +6.2 | 5e-08 | 5/8 (A-172, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +5.9 | 3e-07 | 2/7 (A-172, BT-474) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.22×** | +5.8 | 4e-07 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.74×** | +5.2 | 1e-05 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.04×** | +5.2 | 1e-05 | 3/8 (A-172, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.64×** | +4.8 | 1e-04 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.83×** | +4.4 | 5e-04 | 5/8 (BT-474, A-172, …) | rises with dose | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +4.4 | 5e-04 | 1/5 (hTERT-HPNE) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.34×** | +4.2 | 9e-04 | 1/6 (HS-578T) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +4.2 | 9e-04 | 4/7 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **3.07×** | +4.1 | 0.001 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.06×** | +3.7 | 0.006 | 0/5 | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.52×** | +3.4 | 0.020 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.85×** | +3.2 | 0.042 | 1/5 (HS-578T) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.82×** | +3.1 | 0.050 | 6/7 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.80×** | +3.0 | 0.058 | 4/7 (A-172, BT-474, …) | rises with dose | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.79×** | +3.0 | 0.066 | 0/5 | inconsistent across doses | low cells (technical?); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.21×** | +2.9 | 0.077 | 2/6 (BT-474, A-172) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.48×** | +2.8 | 0.093 | 0/6 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14340.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Abiraterone acetate (drug)]] 0.5 µM |  | 0.517× | -3.4 | 0.34 | 2/8 (BT-474, CFPAC-1) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.537× | -3.1 | 0.38 | 0/8 | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 37.3 | 3 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 5.26× (z +10.4) | — |
| [[A-427 (line)]] | wt | 0.155 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.200 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.224 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.224 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.227 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.198 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.197 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.184 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.194 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.172 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.236 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.164 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.190 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.209 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSG9]] | +0.80 | +0.68 / +0.80 | both halves | 7e-06 | same gene group; pathway: Cell surface interactions at the vascular wall; STRING 778; ⚠ same locus (4.5 kb, same strand: neighbours can correlate without regulation) |
| [[ANKRD30B]] | +0.69 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[SLAMF7]] | +0.69 | +0.65 / +0.63 | both halves | 7e-06 | same gene group |
| [[PSG5]] | +0.64 | +0.40 / +0.71 | both halves | 4e-05 | same gene group; pathway: Cell surface interactions at the vascular wall; STRING 782; ⚠ same locus (6.2 kb, same strand: neighbours can correlate without regulation) |
| [[NGF]] | +0.61 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[GFRA1]] | +0.60 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[LINC02154]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[OLR1]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 | pathway: Cell surface interactions at the vascular wall |
| [[ABCC9]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CLDN16]] | +0.56 | +0.32 / +0.46 | both halves | 1e-04 |  |
| [[MARCOL]] | +0.56 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[LRRN1]] | +0.55 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[GPNMB]] | +0.55 | +0.66 / +0.40 | both halves | 4e-05 |  |
| [[SHISA9]] | +0.54 | +0.61 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGPTL4]] | -0.46 | -0.37 / -0.39 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00958]] | C | LINC00958 activity raises PSG4's level | lines that do not express LINC00958 (39) vs lines expressing it (11) | 1.66× lower at baseline in the lines without LINC00958 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SSX1, LINC01320, LINC00879; co-absent with the target |
| [[ALPK2]] | C | ALPK2 activity raises PSG4's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without ALPK2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[NR1H4]] | C | NR1H4 activity raises PSG4's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 1.61× lower at baseline in the lines without NR1H4 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[PSG5]] | C | PSG5 activity raises PSG4's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 4.12× lower at baseline in the lines without PSG5 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[LAMA1]] | C | LAMA1 activity raises PSG4's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 1.77× lower at baseline in the lines without LAMA1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1; co-absent with the target |
| [[ANKRD30B]] | C | ANKRD30B activity raises PSG4's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 3.16× lower at baseline in the lines without ANKRD30B | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF; co-absent with the target |
| [[LINC02241]] | C | LINC02241 activity raises PSG4's level | lines that do not express LINC02241 (34) vs lines expressing it (16) | 2.05× lower at baseline in the lines without LINC02241 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000259560, LINC02616, LINC02476; maybe low, not absent; co-absent with the target |
| [[PHACTR1]] | C | PHACTR1 activity raises PSG4's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 2.58× lower at baseline in the lines without PHACTR1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L; co-absent with the target |
| [[TRIM58]] | C | TRIM58 activity raises PSG4's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 1.54× lower at baseline in the lines without TRIM58 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20; co-absent with the target |
| [[PSG9]] | C | PSG9 activity raises PSG4's level | lines that do not express PSG9 (45) vs lines expressing it (5) | 8.05× lower at baseline in the lines without PSG9 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, PSG1, NPPB; co-absent with the target |
| [[LINC02154]] | C | LINC02154 activity raises PSG4's level | lines that do not express LINC02154 (37) vs lines expressing it (13) | 2.05× lower at baseline in the lines without LINC02154 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530; co-absent with the target |
| [[ABCC9]] | C | ABCC9 activity raises PSG4's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 1.97× lower at baseline in the lines without ABCC9 | 0.082 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 4, C 14. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESR1]] | B | PSG4 activity raises ESR1's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 2.25× lower at baseline in the lines without PSG4 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5 |
| [[C12orf50]] | B | PSG4 activity raises C12orf50's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 1.99× lower at baseline in the lines without PSG4 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5 |
| [[MIR4300HG]] | B | PSG4 activity raises MIR4300HG's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 1.57× lower at baseline in the lines without PSG4 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5 |
| [[TENM3-AS1]] | B | PSG4 activity raises TENM3-AS1's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 1.66× lower at baseline in the lines without PSG4 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5 |
| [[LINC00504]] | C | PSG4 activity raises LINC00504's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 1.82× lower at baseline in the lines without PSG4 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[LINC02241]] | C | PSG4 activity raises LINC02241's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 2.37× lower at baseline in the lines without PSG4 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[MIR155HG]] | C | PSG4 activity raises MIR155HG's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 3.50× lower at baseline in the lines without PSG4 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[PHACTR1]] | C | PSG4 activity raises PHACTR1's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 2.92× lower at baseline in the lines without PSG4 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[ANKRD30B]] | C | PSG4 activity raises ANKRD30B's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 4.19× lower at baseline in the lines without PSG4 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[COLEC10]] | C | PSG4 activity raises COLEC10's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 1.66× lower at baseline in the lines without PSG4 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[SHISA9]] | C | PSG4 activity raises SHISA9's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 1.79× lower at baseline in the lines without PSG4 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[PNLIPRP3]] | C | PSG4 activity raises PNLIPRP3's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 1.55× lower at baseline in the lines without PSG4 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.7, 22.2); signed map (38.7, 23.4). **Vector** length 25.3, 7.88% of its response variance represented; |z| ≥ 3 in 204 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.8 | -1.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.7 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | pregnancy specific beta-1-glycoprotein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,192,702-43,207,299 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | V-set domain containing; Pregnancy specific glycoproteins |
| Reactome | 2 pathways, smallest: Cell surface interactions at the vascular wall; Hemostasis |
| Matched by | ensembl_id |

UniProt [Q00888](https://www.uniprot.org/uniprotkb/Q00888) carries no function annotation.

**Summary**, from NCBI Gene [5672](https://www.ncbi.nlm.nih.gov/gene/5672):

> The protein encoded by this gene is a pregnancy-specific glycoprotein (PSG), one of several encoded by a cluster of similar genes on chromosome 19. This gene is a member of the carcinoembryonic antigen (CEA) gene family and may play a role in regulation of the innate immune system. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2015]

**Accessions** — [HGNC:9521](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9521) · Entrez [5672](https://www.ncbi.nlm.nih.gov/gene/5672) · UniProt [Q00888](https://www.uniprot.org/uniprotkb/Q00888) · Ensembl [ENSG00000243137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243137)

## Data

Gene col 14340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14340); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14340]; `tensor/DDL_lfc|DDL_z.npy` [14340]; `embed/gene_vectors.npy` [14340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14340 or target_col == 14340). Every well: [[PSG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
