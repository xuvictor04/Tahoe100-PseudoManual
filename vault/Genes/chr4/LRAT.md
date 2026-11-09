---
symbol: "LRAT"
type: "gene"
col: 4257
ensembl_id: "ENSG00000121207"
name: "lecithin retinol acyltransferase"
location: "4q32.1"
module: 152
arm: "+"
pooled_cpm: 20.25
n_lines_expressing: 20
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# LRAT

*lecithin retinol acyltransferase* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.58× (z +8.2, q 1e-13, up in 8 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.430× (z -10.3, q 3e-22, down in 15 of 17 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRD]] (+0.71, fdr 7e-06), [[EPHA3]] (+0.67, fdr 8e-06), [[ADAM12]] (+0.62, fdr 1e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LRRK2]] → it (grade C ⚠); 7 go from it, the strongest it → [[TCAF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4257.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +8.2 | 1e-13 | 8/18 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.5 | 2e-08 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +6.1 | 2e-07 | 2/16 (HEC-1-A, hTERT-HPNE) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +5.7 | 2e-06 | 10/17 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.50×** | +3.7 | 0.029 | 0/17 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.12 | 1/18 (HEC-1-A) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.41× | +3.1 | 0.14 | 1/17 (hTERT-HPNE) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4257.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.430×** | -10.3 | 3e-22 | 15/17 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.452×** | -10.1 | 2e-21 | 15/17 (NCI-H1792, A498, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.633×** | -8.2 | 3e-14 | 16/17 (NCI-H1792, C32, …) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -6.8 | 1e-09 | 15/17 (J82, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.676×** | -5.0 | 7e-05 | 8/17 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.712×** | -4.3 | 0.001 | 9/17 (RPMI-7951, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.719×** | -4.2 | 0.002 | 11/17 (NCI-H460, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[crizotinib (drug)]] 5 µM |  | **0.723×** | -4.0 | 0.005 | 3/17 (C32, A498, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.736×** | -3.9 | 0.005 | 12/17 (C32, CHP-212, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.736×** | -3.9 | 0.005 | 13/17 (RPMI-7951, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.751×** | -3.6 | 0.014 | 7/17 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.610×** | -3.3 | 0.048 | 13/17 (NCI-H1792, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.778×** | -3.2 | 0.060 | 2/17 (A498, NCI-H460) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 335 | 0 | 19 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0703× (z -31.0) |
| [[NCI-H1792 (line)]] | alt | 120 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0287× (z -38.7) |
| [[SK-MEL-2 (line)]] | alt | 154 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0807× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.330× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 10.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -19.1) |
| [[NCI-H1573 (line)]] | alt | 53.9 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.301× (z -10.3) |
| [[A498 (line)]] | wt | 12.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -16.1) |
| [[J82 (line)]] | alt | 16.2 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0654× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.241× (z -10.2) |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0378× (z -15.4) |
| [[NCI-H2030 (line)]] | alt | 81.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -15.5) |
| [[SNU-423 (line)]] | alt | 8.40 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0346× (z -12.6) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.101× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 53.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 7.59 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 5.65 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0367× (z -10.4) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW 900 (line)]] | alt | 9.20 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0928× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[A-172 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.62 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRD]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[EPHA3]] | +0.67 | +0.58 / +0.67 | both halves | 8e-06 | **novel candidate** |
| [[ADAM12]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[LINGO2]] | +0.62 | +0.52 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[LRRC7]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[DPYSL4]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[PI15]] | +0.60 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[SOX10]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PAX3]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[C10orf90]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TDRD9]] | +0.58 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[MDGA2]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRK2]] | C | LRRK2 activity raises LRAT's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 3.73× lower at baseline in the lines without LRRK2 | 0.040 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[ADAMTS9-AS2]] | C | ADAMTS9-AS2 activity raises LRAT's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 4.34× lower at baseline in the lines without ADAMTS9-AS2 | 0.041 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2; co-absent with the target |
| [[IGFBP3]] | C | IGFBP3 activity raises LRAT's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 3.36× lower at baseline in the lines without IGFBP3 | 0.082 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF; co-absent with the target |
| [[NRG3]] | C | NRG3 activity raises LRAT's level | lines that do not express NRG3 (41) vs lines expressing it (9) | 4.09× lower at baseline in the lines without NRG3 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC00879, GPR141; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCAF2]] | B | LRAT activity raises TCAF2's level | lines that do not express LRAT (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without LRAT | 0.042 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, NR0B1, IL6 |
| [[NIM1K]] | B | LRAT activity raises NIM1K's level | lines that do not express LRAT (30) vs lines expressing it (20) | 2.10× lower at baseline in the lines without LRAT | 0.068 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, NR0B1, IL6 |
| [[ITGB3]] | C | LRAT activity raises ITGB3's level | lines that do not express LRAT (30) vs lines expressing it (20) | 5.70× lower at baseline in the lines without LRAT | 0.012 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, NR0B1, IL6; co-absent with the target |
| [[AEBP1]] | C | LRAT activity raises AEBP1's level | lines that do not express LRAT (30) vs lines expressing it (20) | 3.03× lower at baseline in the lines without LRAT | 0.038 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, NR0B1, IL6; co-absent with the target |
| [[STAC]] | C | LRAT activity raises STAC's level | lines that do not express LRAT (30) vs lines expressing it (20) | 4.93× lower at baseline in the lines without LRAT | 0.040 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, NR0B1, IL6; co-absent with the target |
| [[BICC1]] | C | LRAT activity raises BICC1's level | lines that do not express LRAT (30) vs lines expressing it (20) | 4.47× lower at baseline in the lines without LRAT | 0.070 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, NR0B1, IL6; co-absent with the target |
| [[ADAMTS9-AS2]] | C | LRAT activity raises ADAMTS9-AS2's level | lines that do not express LRAT (30) vs lines expressing it (20) | 4.88× lower at baseline in the lines without LRAT | 0.080 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, NR0B1, IL6; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.1, 28.9); signed map (31.8, 41.1). **Vector** length 69.6, 23.7% of its response variance represented; |z| ≥ 3 in 526 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.9 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -6.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.6 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -1.1 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | lecithin retinol acyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:154,626,945-154,753,120 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LCA14 |
| Gene groups (HGNC) | LRAT domain containing ; Acyltransferases |
| Reactome | 9 pathways, smallest: Diseases associated with visual transduction; Diseases of the neuronal system; Retinoid cycle disease events |
| Matched by | ensembl_id |

**Function**, from UniProt [O95237](https://www.uniprot.org/uniprotkb/O95237) (Lecithin retinol acyltransferase):

> Transfers the acyl group from the sn-1 position of phosphatidylcholine to all-trans retinol, producing all-trans retinyl esters. Retinyl esters are storage forms of vitamin A (Probable). LRAT plays a critical role in vision (Probable). It provides the all-trans retinyl ester substrates for the isomerohydrolase which processes the esters into 11-cis-retinol in the retinal pigment epithelium; due to a membrane-associated alcohol dehydrogenase, 11 cis-retinol is oxidized and converted into …

**Summary**, from NCBI Gene [9227](https://www.ncbi.nlm.nih.gov/gene/9227):

> The protein encoded by this gene localizes to the endoplasmic reticulum, where it catalyzes the esterification of all-trans-retinol into all-trans-retinyl ester. This reaction is an important step in vitamin A metabolism in the visual system. Mutations in this gene have been associated with early-onset severe retinal dystrophy and Leber congenital amaurosis 14. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2014]

**Accessions** — [HGNC:6685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6685) · Entrez [9227](https://www.ncbi.nlm.nih.gov/gene/9227) · UniProt [O95237](https://www.uniprot.org/uniprotkb/O95237) · Ensembl [ENSG00000121207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121207)

## Data

Gene col 4257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4257); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4257]; `tensor/DDL_lfc|DDL_z.npy` [4257]; `embed/gene_vectors.npy` [4257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4257 or target_col == 4257). Every well: [[LRAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
