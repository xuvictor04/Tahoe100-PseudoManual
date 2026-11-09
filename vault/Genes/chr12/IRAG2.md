---
symbol: "IRAG2"
type: "gene"
col: 3981
ensembl_id: "ENSG00000118308"
name: "inositol 1,4,5-triphosphate receptor associated 2"
location: "12p12.1"
module: 14
arm: "+"
pooled_cpm: 8.86
n_lines_expressing: 11
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 24
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# IRAG2

*inositol 1,4,5-triphosphate receptor associated 2* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.40× (z +15.8, q 0e+00, up in 5 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HOP62 0.131×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HOP62 0.154×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HOP62 0.235×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00944]] (+0.64, fdr 3e-05), [[JAM2]] (+0.63, fdr 1e-05), [[LINC02605]] (+0.62, fdr 2e-05); moves opposite to [[NAPG]] (-0.54, fdr 3e-05), [[APMAP]] (-0.50, fdr 1e-04), [[ATG5]] (-0.48, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 24 go from it, the strongest it → [[BLTP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.40×** | +15.8 | 0e+00 | 5/7 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.73×** | +14.1 | 2e-42 | 6/8 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +9.2 | 1e-17 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.83×** | +7.8 | 6e-13 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +6.8 | 2e-09 | 3/7 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +5.8 | 5e-07 | 4/8 (HS-578T, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +5.7 | 7e-07 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +5.6 | 2e-06 | 6/8 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +5.4 | 4e-06 | 5/8 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +5.3 | 7e-06 | 5/8 (HS-578T, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +5.2 | 1e-05 | 5/8 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +4.8 | 9e-05 | 3/6 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.7 | 1e-04 | 5/9 (J82, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.81×** | +4.5 | 3e-04 | 1/8 (J82) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.3 | 5e-04 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +3.9 | 0.003 | 5/8 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.57×** | +3.4 | 0.022 | 0/8 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.055 | 2/8 (HS-578T, NCI-H1792) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.056 | 0/8 | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.77×** | +3.1 | 0.056 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3981.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HOP62 0.131×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HOP62 0.154×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HOP62 0.235×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.712× | -3.6 | 0.16 | 4/8 (NCI-H1792, HOP62, …) | inconsistent across doses | position effect removed |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.641× | -3.4 | 0.22 | 1/8 (NCI-H1792) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.643× | -3.1 | 0.37 | 0/8 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 221 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -14.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 7.08 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.4× (z +18.0) | — |
| [[HS-578T (line)]] | alt | 4.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 5.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.5× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 6.07 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0718× (z -8.6) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.741 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.885 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.887 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.997 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.956 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.957 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.875 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00944]] | +0.64 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[JAM2]] | +0.63 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LINC02605]] | +0.62 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[LINC00882]] | +0.58 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[C12orf50]] | +0.58 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[LINC00504]] | +0.58 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[ROR1-AS1]] | +0.58 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[TNFAIP6]] | +0.56 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[SHISAL1]] | +0.55 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[N4BP2L1]] | +0.55 | +0.45 / +0.43 | both halves | 4e-05 |  |
| [[RRAD]] | +0.55 | +0.53 / +0.38 | both halves | 7e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[CCL5]] | +0.55 | +0.57 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPG]] | -0.54 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[APMAP]] | -0.50 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[ATG5]] | -0.48 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[LYPLA1]] | -0.48 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[ELP1]] | -0.48 | -0.34 / -0.31 | both halves | 2e-04 | pathway: HALLMARK_P53_PATHWAY |
| [[FBXW2]] | -0.48 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[CTNNBL1]] | -0.47 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[CHUK]] | -0.47 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[GTF2E2]] | -0.47 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[STRAP]] | -0.47 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[BLTP2]] | -0.47 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[STIMATE]] | -0.46 | -0.32 / -0.34 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IRAG2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TNFAIP6]] | C | TNFAIP6 activity raises IRAG2's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 2.47× lower at baseline in the lines without TNFAIP6 | 0.027 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF; co-absent with the target |
| [[VCAM1]] | C | VCAM1 activity raises IRAG2's level | lines that do not express VCAM1 (40) vs lines expressing it (10) | 2.30× lower at baseline in the lines without VCAM1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, TMPRSS15, GLYATL2; co-absent with the target |
| [[SHISAL1]] | C | SHISAL1 activity raises IRAG2's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 1.99× lower at baseline in the lines without SHISAL1 | 0.056 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[RRAD]] | C | RRAD activity raises IRAG2's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.21× lower at baseline in the lines without RRAD | 0.074 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA; co-absent with the target |
| [[SLC6A7]] | C | SLC6A7 activity raises IRAG2's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without SLC6A7 | 0.083 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9; co-absent with the target |
| [[MIR155HG]] | C | MIR155HG activity raises IRAG2's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 1.88× lower at baseline in the lines without MIR155HG | 0.083 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA; co-absent with the target |
| [[SLC43A3]] | C | SLC43A3 activity raises IRAG2's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 1.88× lower at baseline in the lines without SLC43A3 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 12, C 12. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BLTP2]] | B | IRAG2 activity lowers BLTP2's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 1.39× higher at baseline in the lines without IRAG2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[PLAGL1]] | B | IRAG2 activity raises PLAGL1's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 2.75× lower at baseline in the lines without IRAG2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[LINC00944]] | B | IRAG2 activity raises LINC00944's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 3.74× lower at baseline in the lines without IRAG2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[LINC02100]] | B | IRAG2 activity raises LINC02100's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 2.19× lower at baseline in the lines without IRAG2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[LYPLA1]] | B | IRAG2 activity lowers LYPLA1's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 1.40× higher at baseline in the lines without IRAG2 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[HMGN2P46]] | B | IRAG2 activity raises HMGN2P46's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 4.38× lower at baseline in the lines without IRAG2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[BTN2A3P]] | B | IRAG2 activity raises BTN2A3P's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 1.36× lower at baseline in the lines without IRAG2 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[CHUK]] | B | IRAG2 activity lowers CHUK's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 1.24× higher at baseline in the lines without IRAG2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[LINC02605]] | B | IRAG2 activity raises LINC02605's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 2.31× lower at baseline in the lines without IRAG2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[LINC01828]] | B | IRAG2 activity raises LINC01828's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 2.73× lower at baseline in the lines without IRAG2 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[BTN2A3P-1]] | B | IRAG2 activity raises BTN2A3P-1's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 1.38× lower at baseline in the lines without IRAG2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[MARCKS]] | B | IRAG2 activity raises MARCKS's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 2.84× lower at baseline in the lines without IRAG2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.0, 22.5); signed map (41.2, 23.0). **Vector** length 25.0, 6.93% of its response variance represented; |z| ≥ 3 in 224 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +14.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.5 | +15.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.3 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.1 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.7 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.7 | +2.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -0.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.6 | +0.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.6 | -1.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.6 | -1.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | inositol 1,4,5-triphosphate receptor associated 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:25,004,342-25,108,335 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JAW1; previously LRMP |
| Hallmark sets | P53_PATHWAY |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12912](https://www.uniprot.org/uniprotkb/Q12912) (Inositol 1,4,5-triphosphate receptor associated 2):

> Plays a role in the delivery of peptides to major histocompatibility complex (MHC) class I molecules; this occurs in a transporter associated with antigen processing (TAP)-independent manner. May play a role in taste signal transduction via ITPR3. May play a role during fertilization in pronucleus congression and fusion. Plays a role in maintaining nuclear shape, maybe as a component of the LINC complex and through interaction with microtubules. Plays a role in the regulation of cellular …

**Summary**, from NCBI Gene [4033](https://www.ncbi.nlm.nih.gov/gene/4033):

> The protein encode dby this gene is expressed in a developmentally regulated manner in lymphoid cell lines and tissues. The protein is localized to the cytoplasmic face of the endoplasmic reticulum. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6690](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6690) · Entrez [4033](https://www.ncbi.nlm.nih.gov/gene/4033) · UniProt [Q12912](https://www.uniprot.org/uniprotkb/Q12912) · Ensembl [ENSG00000118308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118308)

## Data

Gene col 3981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3981); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3981]; `tensor/DDL_lfc|DDL_z.npy` [3981]; `embed/gene_vectors.npy` [3981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3981 or target_col == 3981). Every well: [[IRAG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRAG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
