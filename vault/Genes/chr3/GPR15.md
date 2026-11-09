---
symbol: "GPR15"
type: "gene"
col: 7780
ensembl_id: "ENSG00000154165"
name: "G protein-coupled receptor 15"
location: "3q11.2"
module: 27
arm: "+"
pooled_cpm: 3.07
n_lines_expressing: 4
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 11
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# GPR15

*G protein-coupled receptor 15* — 3q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.01× (z +9.1, q 7e-17, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.91× (z +4.1, q 0.002, up in 0 of 2 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.0306×, A-427 0.196×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.0814×); [[Auranofin (drug)]] 5 µM in 1 line (SW48 0.0597×); [[Bortezomib (drug)]] 0.05 µM in 1 line (SW48 0.0901×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAT3]] (+0.68, fdr 1e-05), [[FGF20]] (+0.49, fdr 3e-04), [[PPP1R9A]] (+0.48, fdr 5e-04); moves opposite to [[ABCD1]] (-0.44, fdr 5e-05), [[GHRLOS]] (-0.40, fdr 2e-04), [[SPSB1]] (-0.39, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GNAT3]] → it (grade C ⚠); 11 go from it, the strongest it → [[CD36]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7780.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.01×** | +9.1 | 7e-17 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.70×** | +7.9 | 9e-13 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.48×** | +7.1 | 2e-10 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.18×** | +5.2 | 2e-05 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.60×** | +4.9 | 9e-05 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.70×** | +4.5 | 7e-04 | 0/2 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.66×** | +4.2 | 0.002 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.54×** | +4.2 | 0.002 | 1/2 (A-427) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.91×** | +4.1 | 0.002 | 0/2 | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **3.51×** | +4.1 | 0.003 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +4.0 | 0.003 | 1/2 (A-427) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.38×** | +3.9 | 0.004 | 0/2 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **5.23×** | +3.9 | 0.004 | 0/1 | top dose only | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +3.9 | 0.004 | 1/2 (A-427) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.71×** | +3.4 | 0.024 | 1/2 (A-427) | top dose only | composition shift |
| [[Saquinavir (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.025 | 1/2 (A-427) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.84×** | +3.4 | 0.025 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.95×** | +3.0 | 0.083 | 0/2 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.0 | 0.091 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.58×** | +2.9 | 0.100 | 0/2 | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7780.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.0306×, A-427 0.196×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.0814×); [[Auranofin (drug)]] 5 µM in 1 line (SW48 0.0597×); [[Bortezomib (drug)]] 0.05 µM in 1 line (SW48 0.0901×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.481× | -3.4 | 0.46 | 0/2 | inconsistent across doses | position effect removed |
| [[Asciminib (drug)]] 0.5 µM |  | 0.516× | -3.0 | 0.55 | 0/2 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7780. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 123 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0814× (z -14.6) |
| [[A-427 (line)]] | wt | 82.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.217 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.175 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.170 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.237 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.207 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.219 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.287 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.206 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.281 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.207 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.224 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.256 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.205 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.207 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.175 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.237 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.207 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7780), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 9 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAT3]] | +0.68 | +0.50 / +0.60 | both halves | 1e-05 | pathway: G alpha (s) signalling events |
| [[FGF20]] | +0.49 | +0.28 / +0.57 | both halves | 3e-04 |  |
| [[PPP1R9A]] | +0.48 | +0.23 / +0.62 | both halves | 5e-04 |  |
| [[AXIN2]] | +0.48 | +0.28 / +0.52 | both halves | 3e-04 |  |
| [[ARL2]] | +0.46 | +0.22 / +0.46 | both halves | 6e-04 |  |
| [[COQ2]] | +0.46 | +0.33 / +0.43 | both halves | 1e-04 |  |
| [[LINC01956]] | +0.44 | +0.40 / +0.58 | both halves | 4e-05 |  |
| [[LINC02832]] | +0.43 | +0.31 / +0.40 | both halves | 2e-04 |  |
| [[NUDCD2]] | +0.43 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[EDN1]] | +0.43 | +0.27 / +0.38 | both halves | 3e-04 |  |
| [[KLRC3]] | +0.42 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[ARL4A]] | +0.42 | +0.30 / +0.42 | both halves | 2e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCD1]] | -0.44 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[GHRLOS]] | -0.40 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[SPSB1]] | -0.39 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[TPD52L2]] | -0.37 | -0.26 / -0.35 | both halves | 4e-04 |  |
| [[PEX6]] | -0.35 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[SEC14L2]] | -0.35 | -0.24 / -0.33 | both halves | 4e-04 |  |
| [[MAP2K1]] | -0.35 | -0.32 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAT3]] | C | GNAT3 activity raises GPR15's level | lines that do not express GNAT3 (32) vs lines expressing it (18) | 1.87× lower at baseline in the lines without GNAT3 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MEOX2, IHO1, ZFHX4-AS1; maybe low, not absent; co-absent with the target |
| [[FGF20]] | C | FGF20 activity raises GPR15's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 3.19× lower at baseline in the lines without FGF20 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises GPR15's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.35× lower at baseline in the lines without KCNB2 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD36]] | C | GPR15 activity raises CD36's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 10.94× lower at baseline in the lines without GPR15 | 0.001 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10; co-absent with the target |
| [[GNAT3]] | C | GPR15 activity raises GNAT3's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 5.49× lower at baseline in the lines without GPR15 | 0.002 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10; co-absent with the target |
| [[AXIN2]] | C | GPR15 activity raises AXIN2's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 8.67× lower at baseline in the lines without GPR15 | 0.003 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10; co-absent with the target |
| [[FGF20]] | C | GPR15 activity raises FGF20's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 6.31× lower at baseline in the lines without GPR15 | 0.007 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10; co-absent with the target |
| [[OVOL2]] | C | GPR15 activity raises OVOL2's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 2.14× lower at baseline in the lines without GPR15 | 0.029 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10 |
| [[BAMBI]] | C | GPR15 activity raises BAMBI's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 3.01× lower at baseline in the lines without GPR15 | 0.047 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10 |
| [[KSR2]] | C | GPR15 activity raises KSR2's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 6.54× lower at baseline in the lines without GPR15 | 0.048 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10 |
| [[EDAR]] | C | GPR15 activity raises EDAR's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 3.55× lower at baseline in the lines without GPR15 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10; co-absent with the target |
| [[LINC01956]] | C | GPR15 activity raises LINC01956's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 4.19× lower at baseline in the lines without GPR15 | 0.063 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10; co-absent with the target |
| [[BMP4]] | C | GPR15 activity raises BMP4's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 3.87× lower at baseline in the lines without GPR15 | 0.074 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10; co-absent with the target |
| [[RNF43]] | C | GPR15 activity raises RNF43's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 4.86× lower at baseline in the lines without GPR15 | 0.0998 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.347). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.3, 41.5); signed map (61.9, 19.6). **Vector** length 11.6, 5.31% of its response variance represented; |z| ≥ 3 in 68 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.8 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.8 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.7 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.6 | +3.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +0.6 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.4 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.4 | +4.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +0.3 | +2.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.3 | +2.1 |
|  | [[AZD-7648 (drug)]] 5 µM |  | +0.3 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.3 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.2 | +1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.2 | -0.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.2 | -2.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.2 | -2.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q11.2 — chr3:98,531,978-98,534,681 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | G protein-coupled receptors, Class A orphans |
| Reactome | 3 pathways, smallest: G alpha (s) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [P49685](https://www.uniprot.org/uniprotkb/P49685) (G protein-coupled receptor 15):

> G protein-coupled receptor that plays an important role in immune homeostasis. Acts via its natural ligand GPR15LG, a chemokine-like polypeptide strongly expressed in gastrointestinal tissues. GPR15-GPR15LG signaling axis regulates intestinal homeostasis and inflammation through the migration of immune cells. Controls thereby the specific homing of T-cells, particularly FOXP3+ regulatory T-cells (Tregs), to the large intestine lamina propria (By similarity). Also required for skin localization …

**Summary**, from NCBI Gene [2838](https://www.ncbi.nlm.nih.gov/gene/2838):

> This gene encodes a G protein-coupled receptor that acts as a chemokine receptor for human immunodeficiency virus type 1 and 2. The encoded protein localizes to the cell membrane. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:4469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4469) · Entrez [2838](https://www.ncbi.nlm.nih.gov/gene/2838) · UniProt [P49685](https://www.uniprot.org/uniprotkb/P49685) · Ensembl [ENSG00000154165](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154165)

## Data

Gene col 7780: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7780); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7780, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7780]; `tensor/DDL_lfc|DDL_z.npy` [7780]; `embed/gene_vectors.npy` [7780]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7780 or target_col == 7780). Every well: [[GPR15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPR15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
