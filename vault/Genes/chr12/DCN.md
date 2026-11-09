---
symbol: "DCN"
type: "gene"
col: 243
ensembl_id: "ENSG00000011465"
name: "decorin"
location: "12q21.33"
module: 104
arm: "+"
pooled_cpm: 4.65
n_lines_expressing: 11
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# DCN

*decorin* — 12q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 10.6× (z +12.4, q 1e-32, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.32× (z +6.5, q 1e-08, up in 2 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RPMI-7951 0.0678×, NCI-H1792 0.115×; ⚠ cell-cycle shift, explains ~91% of this change); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0310×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0565×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0672×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSD11B1]] (+0.74, fdr 7e-06), [[IRAK3]] (+0.69, fdr 7e-06), [[DNER]] (+0.67, fdr 7e-06); moves opposite to [[TCP10L]] (-0.49, fdr 5e-05), [[LINC00973]] (-0.47, fdr 1e-04), [[IL11]] (-0.47, fdr 1e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 9 go from it, the strongest it → [[CCN4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 243.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **10.6×** | +12.4 | 1e-32 | 3/4 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.82×** | +10.5 | 2e-23 | 2/5 (hTERT-HPNE, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.86×** | +8.0 | 2e-13 | 3/4 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +6.5 | 1e-08 | 2/6 (HS-578T, hTERT-HPNE) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **3.04×** | +6.1 | 1e-07 | 5/7 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.23×** | +4.4 | 0.001 | 5/7 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.74×** | +4.3 | 0.002 | 5/7 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +4.2 | 0.002 | 0/5 | top dose only | cell-cycle shift (explains ~9% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.17×** | +4.2 | 0.002 | 5/7 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +4.1 | 0.003 | 4/7 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.11×** | +3.9 | 0.004 | 6/7 (HS-578T, NCI-H1792, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.82×** | +3.8 | 0.006 | 2/3 (HS-578T, hTERT-HPNE) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.99×** | +3.8 | 0.007 | 5/6 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +3.7 | 0.007 | 6/7 (HS-578T, RPMI-7951, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.95×** | +3.6 | 0.012 | 6/7 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +3.5 | 0.017 | 4/6 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.60×** | +3.3 | 0.029 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.034 | 2/7 (hTERT-HPNE, HS-578T) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.81×** | +3.3 | 0.034 | 5/7 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.69×** | +2.9 | 0.099 | 5/7 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 243.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RPMI-7951 0.0678×, NCI-H1792 0.115×; ⚠ cell-cycle shift, explains ~91% of this change); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0310×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0565×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0672×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.559× | -3.1 | 0.98 | 0/7 | rises with dose | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 68.3 | 0 | 8 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0310× (z -13.8) |
| [[HS-578T (line)]] | alt | 51.5 | 1 | 0 | [[Dexamethasone (drug)]] 5 µM 5.88× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0678× (z -14.2) ⚠ cell-cycle shift, explains ~91% of this change |
| [[A-172 (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.663 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.633 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.604 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.782 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD11B1]] | +0.74 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[IRAK3]] | +0.69 | +0.68 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[DNER]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[MGP]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 597 |
| [[PID1]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[TMTC1]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[ITGA8]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 | pathway: ECM proteoglycans |
| [[NPR3]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[HTRA3]] | +0.62 | +0.72 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[LOX]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 616 |
| [[TLR2]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 | STRING 990 |
| [[DAAM2]] | +0.60 | +0.42 / +0.65 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCP10L]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[LINC00973]] | -0.47 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[IL11]] | -0.47 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[C2CD2]] | -0.46 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[STARD8]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[AFF3]] | -0.45 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[CSF2]] | -0.44 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[FGF5]] | -0.44 | -0.31 / -0.42 | both halves | 2e-04 | STRING 905 |
| [[GDNF]] | -0.43 | -0.23 / -0.57 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises DCN's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[RNF175]] | C | RNF175 activity raises DCN's level | lines that do not express RNF175 (30) vs lines expressing it (20) | 3.29× lower at baseline in the lines without RNF175 | 0.010 | ⚠ within organs, on part of the lines; also absent: SCG2, ENSG00000266450, MIR493HG; co-absent with the target |
| [[HTRA3]] | C | HTRA3 activity raises DCN's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 3.27× lower at baseline in the lines without HTRA3 | 0.027 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises DCN's level | lines that do not express GDNF (38) vs lines expressing it (12) | 3.53× lower at baseline in the lines without GDNF | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[LOX]] | C | LOX activity raises DCN's level | lines that do not express LOX (31) vs lines expressing it (19) | 3.08× lower at baseline in the lines without LOX | 0.049 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; co-absent with the target |
| [[PDGFRA]] | C | PDGFRA activity raises DCN's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 2.99× lower at baseline in the lines without PDGFRA | 0.050 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1; co-absent with the target |
| [[SLC7A2]] | C | SLC7A2 activity raises DCN's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without SLC7A2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D; co-absent with the target |
| [[TLR2]] | C | TLR2 activity raises DCN's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 2.39× lower at baseline in the lines without TLR2 | 0.060 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA; co-absent with the target |
| [[DNER]] | C | DNER activity raises DCN's level | lines that do not express DNER (32) vs lines expressing it (18) | 3.52× lower at baseline in the lines without DNER | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC; co-absent with the target |
| [[IRAK3]] | C | IRAK3 activity raises DCN's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 2.10× lower at baseline in the lines without IRAK3 | 0.089 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5; co-absent with the target |
| [[BICC1]] | C | BICC1 activity raises DCN's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.61× lower at baseline in the lines without BICC1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN4]] | B | DCN activity raises CCN4's level | lines that do not express DCN (39) vs lines expressing it (11) | 3.10× lower at baseline in the lines without DCN | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1 |
| [[ADPRHL1]] | B | DCN activity raises ADPRHL1's level | lines that do not express DCN (39) vs lines expressing it (11) | 1.87× lower at baseline in the lines without DCN | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1 |
| [[CCN4]] | B | DCN activity weakens CCN4's drug response | lines that do not express DCN (37) vs lines expressing it (8) | the lines without DCN respond 1.00× as strongly (z diff +0.17); strongest at Dinaciclib 0.5 µM: 3.10x vs 0.30x (z diff -8.1) | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1; target measured in part of the lines; both ways; artifact flags |
| [[LTBP1]] | B | DCN activity raises LTBP1's level | lines that do not express DCN (39) vs lines expressing it (11) | 3.21× lower at baseline in the lines without DCN | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1 |
| [[RUNX2]] | B | DCN activity raises RUNX2's level | lines that do not express DCN (39) vs lines expressing it (11) | 2.37× lower at baseline in the lines without DCN | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1 |
| [[PDGFRA]] | C | DCN activity raises PDGFRA's level | lines that do not express DCN (39) vs lines expressing it (11) | 4.53× lower at baseline in the lines without DCN | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1; co-absent with the target |
| [[ANPEP]] | C | DCN activity raises ANPEP's level | lines that do not express DCN (39) vs lines expressing it (11) | 3.29× lower at baseline in the lines without DCN | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1; co-absent with the target |
| [[PTGFR]] | C | DCN activity raises PTGFR's level | lines that do not express DCN (39) vs lines expressing it (11) | 4.71× lower at baseline in the lines without DCN | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1; co-absent with the target |
| [[TWIST1]] | C | DCN activity raises TWIST1's level | lines that do not express DCN (39) vs lines expressing it (11) | 5.57× lower at baseline in the lines without DCN | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.818). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.6, 16.6); signed map (18.9, 32.2). **Vector** length 36.7, 14.9% of its response variance represented; |z| ≥ 3 in 237 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +10.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.6 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +6.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.5 | +4.4 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.7 | -0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.7 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.7 | +0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | decorin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.33 — chr12:91,140,484-91,183,217 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DSPG2, SLRR1B |
| Gene groups (HGNC) | Small leucine rich repeat proteoglycans |
| Hallmark sets | APOPTOSIS, GLYCOLYSIS, HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 19 pathways, smallest: Defective CHST14 causes EDS, musculocontractural type; Defective CHST3 causes SEDCJD; Defective CHSY1 causes TPBS |
| Matched by | ensembl_id |

**Function**, from UniProt [P07585](https://www.uniprot.org/uniprotkb/P07585) (Decorin):

> May affect the rate of fibrils formation.

**Summary**, from NCBI Gene [1634](https://www.ncbi.nlm.nih.gov/gene/1634):

> This gene encodes a member of the small leucine-rich proteoglycan family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature protein. This protein plays a role in collagen fibril assembly. Binding of this protein to multiple cell surface receptors mediates its role in tumor suppression, including a stimulatory effect on autophagy and inflammation and an inhibitory effect …

**Accessions** — [HGNC:2705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2705) · Entrez [1634](https://www.ncbi.nlm.nih.gov/gene/1634) · UniProt [P07585](https://www.uniprot.org/uniprotkb/P07585) · Ensembl [ENSG00000011465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011465)

## Data

Gene col 243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 243); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 243]; `tensor/DDL_lfc|DDL_z.npy` [243]; `embed/gene_vectors.npy` [243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 243 or target_col == 243). Every well: [[DCN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
