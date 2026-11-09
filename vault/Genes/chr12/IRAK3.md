---
symbol: "IRAK3"
type: "gene"
col: 1620
ensembl_id: "ENSG00000090376"
name: "interleukin 1 receptor associated kinase 3"
location: "12q14.3"
module: 104
arm: "+"
pooled_cpm: 25.9
n_lines_expressing: 14
n_dd_up: 38
n_dd_down: 7
n_dd_up_clean: 34
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 12
direction_downstream: 11
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# IRAK3

*interleukin 1 receptor associated kinase 3* — 12q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.56× (z +14.5, q 6e-45, up in 0 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.651× (z -4.6, q 0.002, down in 6 of 12 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.685× (z -4.1, q 0.012, down in 7 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLR2]] (+0.82, fdr 7e-06), [[SAA1]] (+0.72, fdr 1e-05), [[TSC22D3]] (+0.72, fdr 7e-06); moves opposite to [[PLAU]] (-0.55, fdr 1e-05), [[PTHLH]] (-0.51, fdr 3e-05), [[HHIP]] (-0.49, fdr 4e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TSC22D3]] → it (grade B ⚠); 11 go from it, the strongest it → [[SLIT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +14.5 | 6e-45 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **3.51×** | +13.7 | 3e-40 | 12/12 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.67×** | +10.7 | 1e-24 | 11/12 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.65×** | +10.7 | 2e-24 | 12/12 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.60×** | +10.4 | 2e-23 | 10/12 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.96×** | +10.4 | 2e-23 | 10/12 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.54×** | +10.2 | 2e-22 | 10/12 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +9.8 | 7e-21 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.60×** | +9.6 | 3e-20 | 11/12 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.50×** | +9.6 | 4e-20 | 10/12 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.38×** | +9.5 | 2e-19 | 10/12 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +8.8 | 8e-17 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +8.2 | 1e-14 | 9/12 (HOP62, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +7.7 | 6e-13 | 10/12 (NCI-H1792, HOP62, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **2.01×** | +7.6 | 9e-13 | 10/12 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **2.08×** | +7.6 | 1e-12 | 10/12 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.95×** | +7.3 | 9e-12 | 10/12 (HOP62, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1620.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.651×** | -4.6 | 0.002 | 6/12 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.685×** | -4.1 | 0.012 | 7/12 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.721×** | -3.5 | 0.055 | 6/12 (CFPAC-1, NCI-H1792, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.722×** | -3.5 | 0.055 | 1/12 (Hs 766T) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.706×** | -3.5 | 0.055 | 0/12 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.710×** | -3.4 | 0.057 | 0/12 | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.733×** | -3.4 | 0.063 | 8/12 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.732× | -3.1 | 0.13 | 0/12 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 178 | 21 | 9 (7 ⚠) | [[Triamcinolone (drug)]] 5 µM 3.84× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -14.9) |
| [[SW 900 (line)]] | alt | 301 | 15 | 15 (9 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.89× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0443× (z -24.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -19.2) |
| [[RPMI-7951 (line)]] | alt | 168 | 18 | 9 (6 ⚠) | [[Triamcinolone (drug)]] 5 µM 3.48× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.0440× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 395 | 0 | 19 (13 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -19.8) |
| [[HOP62 (line)]] | alt | 20.7 | 19 | 0 | [[Triamcinolone (drug)]] 5 µM 9.11× (z +16.6) | — |
| [[AsPC-1 (line)]] | alt | 20.1 | 17 | 1 | [[Budesonide (drug)]] 0.5 µM 9.54× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -10.5) |
| [[Hs 766T (line)]] | wt | 10.9 | 17 | 0 | [[Triamcinolone (drug)]] 5 µM 11.7× (z +13.2) | — |
| [[Panc 03.27 (line)]] | alt | 19.1 | 13 | 0 | [[Budesonide (drug)]] 5 µM 9.70× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.68 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.34 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLR2]] | +0.82 | +0.74 / +0.83 | both halves | 7e-06 | pathway: MyD88:MAL(TIRAP) cascade initiated on plasma membrane; STRING 852 |
| [[SAA1]] | +0.72 | +0.55 / +0.73 | both halves | 1e-05 | pathway: Interleukin-1 family signaling |
| [[TSC22D3]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SAA2]] | +0.69 | +0.55 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[DCN]] | +0.69 | +0.68 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[JPH2]] | +0.69 | +0.57 / +0.71 | both halves | 9e-06 | **novel candidate** |
| [[KLF9]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[VSTM2L]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[NNMT]] | +0.68 | +0.63 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[SAA4]] | +0.67 | +0.55 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[ACSL1]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SAA2-SAA4]] | +0.66 | +0.53 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAU]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PTHLH]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[HHIP]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SLIT2]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 | same gene group |
| [[SLC7A11-AS1]] | -0.47 | -0.39 / -0.46 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 3, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSC22D3]] | B | TSC22D3 activity raises IRAK3's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 2.27× lower at baseline in the lines without TSC22D3 | 0.068 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[LINC02015]] | B | LINC02015 activity raises IRAK3's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 1.99× lower at baseline in the lines without LINC02015 | 0.083 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN |
| [[NR3C1]] | B | NR3C1 activity raises IRAK3's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.7% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[LOX]] | C | LOX activity raises IRAK3's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.99× lower at baseline in the lines without LOX | 0.016 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; co-absent with the target |
| [[TRBC2]] | C | TRBC2 activity raises IRAK3's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 5.22× lower at baseline in the lines without TRBC2 | 0.016 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1; co-absent with the target |
| [[CP]] | C | CP activity raises IRAK3's level | lines that do not express CP (39) vs lines expressing it (11) | 3.62× lower at baseline in the lines without CP | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB; co-absent with the target |
| [[MT1M]] | C | MT1M activity raises IRAK3's level | lines that do not express MT1M (29) vs lines expressing it (21) | 3.33× lower at baseline in the lines without MT1M | 0.046 | ⚠ within organs, on part of the lines; also absent: IRAK3, MIR155HG, G0S2; co-absent with the target |
| [[RHCG]] | C | RHCG activity raises IRAK3's level | lines that do not express RHCG (33) vs lines expressing it (17) | 4.48× lower at baseline in the lines without RHCG | 0.050 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10; co-absent with the target |
| [[TLR2]] | C | TLR2 activity raises IRAK3's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 2.95× lower at baseline in the lines without TLR2 | 0.060 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA; co-absent with the target |
| [[CD38]] | C | CD38 activity raises IRAK3's level | lines that do not express CD38 (35) vs lines expressing it (15) | 4.16× lower at baseline in the lines without CD38 | 0.074 | ⚠ within organs, on part of the lines; also absent: MAGEA10, RNF17, GRIA2; maybe low, not absent; co-absent with the target |
| [[MT1E]] | C | MT1E activity raises IRAK3's level | lines that do not express MT1E (22) vs lines expressing it (28) | 2.82× lower at baseline in the lines without MT1E | 0.083 | ⚠ within organs, on part of the lines; also absent: MT1M, ENSG00000291105, ACSL5; co-absent with the target |
| [[BICC1]] | C | BICC1 activity raises IRAK3's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.69× lower at baseline in the lines without BICC1 | 0.090 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLIT2]] | B | IRAK3 activity raises SLIT2's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 2.44× lower at baseline in the lines without IRAK3 | 0.007 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5 |
| [[RNF165]] | B | IRAK3 activity raises RNF165's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 1.88× lower at baseline in the lines without IRAK3 | 0.011 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5 |
| [[B4GALT1]] | B | IRAK3 activity raises B4GALT1's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 1.50× lower at baseline in the lines without IRAK3 | 0.055 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5 |
| [[TRAM2]] | B | IRAK3 activity raises TRAM2's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 1.43× lower at baseline in the lines without IRAK3 | 0.060 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5 |
| [[HPS5]] | B | IRAK3 activity lowers HPS5's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 1.17× higher at baseline in the lines without IRAK3 | 0.083 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5 |
| [[ARHGAP21]] | B | IRAK3 activity raises ARHGAP21's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 1.41× lower at baseline in the lines without IRAK3 | 0.094 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5 |
| [[TRBC2]] | C | IRAK3 activity raises TRBC2's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 2.85× lower at baseline in the lines without IRAK3 | 0.016 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5; co-absent with the target |
| [[LOX]] | C | IRAK3 activity raises LOX's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 3.10× lower at baseline in the lines without IRAK3 | 0.016 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5; co-absent with the target |
| [[SNAI2]] | C | IRAK3 activity raises SNAI2's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 2.87× lower at baseline in the lines without IRAK3 | 0.054 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5; co-absent with the target |
| [[HTRA3]] | C | IRAK3 activity raises HTRA3's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 2.06× lower at baseline in the lines without IRAK3 | 0.065 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5; co-absent with the target |
| [[DCN]] | C | IRAK3 activity raises DCN's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 2.10× lower at baseline in the lines without IRAK3 | 0.089 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.2, 15.9); signed map (17.2, 30.4). **Vector** length 82.9, 29.9% of its response variance represented; |z| ≥ 3 in 555 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Budesonide (drug)]] 0.5 µM |  | +4.1 | +10.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.0 | +10.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.9 | +10.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.9 | +10.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.9 | +13.7 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.3 | -3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[9-ING-41 (drug)]] 0.05 µM |  | -1.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 1 receptor associated kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.3 — chr12:66,189,195-66,254,622 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IRAK-M |
| Gene groups (HGNC) | Pseudokinases; MicroRNA protein coding host genes; Interleukin 1 receptor associated kinase family |
| Reactome | 11 pathways, smallest: Interleukin-1 signaling; MyD88:MAL(TIRAP) cascade initiated on plasma membrane; Toll Like Receptor TLR6:TLR2 Cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y616](https://www.uniprot.org/uniprotkb/Q9Y616) (Interleukin-1 receptor-associated kinase 3):

> Putative inactive protein kinase which regulates signaling downstream of immune receptors including IL1R and Toll-like receptors. Inhibits dissociation of IRAK1 and IRAK4 from the Toll-like receptor signaling complex by either inhibiting the phosphorylation of IRAK1 and IRAK4 or stabilizing the receptor complex (By similarity). Upon IL33-induced lung inflammation, positively regulates expression of IL6, CSF3, CXCL2 and CCL5 mRNAs in dendritic cells.

**Summary**, from NCBI Gene [11213](https://www.ncbi.nlm.nih.gov/gene/11213):

> This gene encodes a member of the interleukin-1 receptor-associated kinase protein family. Members of this family are essential components of the Toll/IL-R immune signal transduction pathways. This protein is primarily expressed in monocytes and macrophages and functions as a negative regulator of Toll-like receptor signaling. Mutations in this gene are associated with a susceptibility to asthma. Alternate splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:17020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17020) · Entrez [11213](https://www.ncbi.nlm.nih.gov/gene/11213) · UniProt [Q9Y616](https://www.uniprot.org/uniprotkb/Q9Y616) · Ensembl [ENSG00000090376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090376)

## Data

Gene col 1620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1620); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1620]; `tensor/DDL_lfc|DDL_z.npy` [1620]; `embed/gene_vectors.npy` [1620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1620 or target_col == 1620). Every well: [[IRAK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRAK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
