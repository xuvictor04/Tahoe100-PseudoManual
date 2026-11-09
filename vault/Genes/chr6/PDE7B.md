---
symbol: "PDE7B"
type: "gene"
col: 10101
ensembl_id: "ENSG00000171408"
name: "phosphodiesterase 7B"
location: "6q23.3"
module: 19
arm: "+"
pooled_cpm: 29.19
n_lines_expressing: 24
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 23
direction_downstream: 14
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PDE7B

*phosphodiesterase 7B* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.41× (z +8.5, q 1e-14, up in 5 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +8.2, q 5e-14, up in 2 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 0.605× (z -4.8, q 1e-03, down in 13 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH11]] (+0.77, fdr 7e-06), [[CDH7]] (+0.76, fdr 7e-06), [[COL4A6]] (+0.76, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[PLAC4]] → it (grade B ⚠); 14 go from it, the strongest it → cells under [[Alpelisib (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10101.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +8.5 | 1e-14 | 5/16 (C32, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +8.2 | 5e-14 | 2/20 (SK-MEL-2, C32) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +7.3 | 7e-11 | 6/22 (SK-MEL-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +5.2 | 3e-05 | 7/22 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.61×** | +4.6 | 4e-04 | 10/21 (KATO III, NCI-H23, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.4 | 0.001 | 2/15 (AsPC-1, H4) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +4.1 | 0.003 | 1/15 (AsPC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Arbutin (drug)]] 0.05 µM |  | **1.55×** | +3.9 | 0.006 | 7/21 (C32, Hs 766T, …) | all doses, flat | position effect removed |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.46×** | +3.7 | 0.014 | 9/21 (SNU-1, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.042 | 5/22 (SW 900, NCI-H23, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.92×** | +3.3 | 0.051 | 6/19 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **1.89×** | +3.2 | 0.064 | 7/20 (HOP62, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.38× | +3.0 | 0.11 | 1/21 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10101.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.605×** | -4.8 | 1e-03 | 13/20 (SW 900, NCI-H23, …) | two highest doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.625×** | -4.5 | 0.002 | 7/21 (SHP-77, HOP62, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.644×** | -4.2 | 0.005 | 12/21 (SHP-77, KATO III, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.645×** | -4.0 | 0.008 | 11/22 (SHP-77, NCI-H460, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.670×** | -3.8 | 0.016 | 8/21 (A549, Hs 766T, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.680×** | -3.7 | 0.022 | 10/21 (NCI-H23, SW 900, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.682×** | -3.6 | 0.022 | 11/21 (NCI-H460, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.780×** | -3.3 | 0.063 | 6/22 (CHP-212, NCI-H1792, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.783×** | -3.3 | 0.068 | 14/22 (NCI-H23, NCI-H460, …) | two highest doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.719×** | -3.1 | 0.095 | 5/21 (C32, HS-578T, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.713× | -3.1 | 0.10 | 10/21 (NCI-H23, SHP-77, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.727× | -3.0 | 0.11 | 8/21 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.729× | -3.0 | 0.11 | 8/21 (A549, SW 900, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.729× | -3.0 | 0.11 | 8/21 (SHP-77, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 311 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -16.0) |
| [[SHP-77 (line)]] | alt | 43.1 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -16.0) |
| [[A549 (line)]] | wt | 83.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -10.8) |
| [[KATO III (line)]] | alt | 17.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[NCI-H1792 (line)]] | alt | 74.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0941× (z -15.1) |
| [[SNU-1 (line)]] | wt | 165 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0793× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -12.2) |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0663× (z -8.7) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 47.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +13.7) | — |
| [[SW 900 (line)]] | alt | 30.4 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0909× (z -9.4) ⚠ cell-cycle shift, explains ~14% of this change |
| [[A-172 (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.68 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.24 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.78 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.83 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 77.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.82 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.73 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH11]] | +0.77 | +0.66 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CDH7]] | +0.76 | +0.71 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[COL4A6]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PDE4B]] | +0.72 | +0.74 / +0.70 | both halves | 7e-06 | same gene group |
| [[GREM2]] | +0.70 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[KCNK2]] | +0.69 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[GLP2R]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 | pathway: G alpha (s) signalling events |
| [[PALMD]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[PDE3A]] | +0.66 | +0.58 / +0.71 | both halves | 7e-06 | same gene group; pathway: G alpha (s) signalling events |
| [[SMOC1]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[TCF4]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 2, C 21. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAC4]] | B | PLAC4 activity raises PDE7B's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 2.24× lower at baseline in the lines without PLAC4 | 0.047 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[SOX6]] | B | SOX6 activity raises PDE7B's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.90× lower at baseline in the lines without SOX6 | 0.059 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[TCF4]] | C | TCF4 activity raises PDE7B's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 3.62× lower at baseline in the lines without TCF4 | 0.001 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[BMPER]] | C | BMPER activity raises PDE7B's level | lines that do not express BMPER (21) vs lines expressing it (29) | 3.03× lower at baseline in the lines without BMPER | 0.005 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R; co-absent with the target |
| [[LINC02994]] | C | LINC02994 activity raises PDE7B's level | lines that do not express LINC02994 (33) vs lines expressing it (17) | 2.27× lower at baseline in the lines without LINC02994 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, ANKRD30B, ENSG00000287598; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises PDE7B's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 3.09× lower at baseline in the lines without PAPPA | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises PDE7B's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 2.23× lower at baseline in the lines without C5orf46 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[TRPA1]] | C | TRPA1 activity raises PDE7B's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 2.88× lower at baseline in the lines without TRPA1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises PDE7B's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.17× lower at baseline in the lines without KCNE4 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[GJA1]] | C | GJA1 activity raises PDE7B's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 2.41× lower at baseline in the lines without GJA1 | 0.026 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; co-absent with the target |
| [[FENDRR]] | C | FENDRR activity raises PDE7B's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 3.67× lower at baseline in the lines without FENDRR | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[TNFRSF11B]] | C | TNFRSF11B activity raises PDE7B's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 2.44× lower at baseline in the lines without TNFRSF11B | 0.031 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 3, C 11. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Alpelisib (drug)]] 5 µM | B | PDE7B activity lowers the cells' numbers under Alpelisib 5 µM (makes them more sensitive) | lines that do not express PDE7B (26) vs lines expressing it (22) | the lines without PDE7B: 1.31× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent |
| [[PDE4D]] | B | PDE7B activity raises PDE4D's level | lines that do not express PDE7B (26) vs lines expressing it (24) | 1.91× lower at baseline in the lines without PDE7B | 0.077 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | B | PDE7B activity lowers the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (makes them more sensitive) | lines that do not express PDE7B (26) vs lines expressing it (22) | the lines without PDE7B: 1.09× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent |
| [[KCNK2]] | C | PDE7B activity raises KCNK2's level | lines that do not express PDE7B (26) vs lines expressing it (24) | 2.16× lower at baseline in the lines without PDE7B | 0.023 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent; co-absent with the target |
| [[GNG11]] | C | PDE7B activity raises GNG11's level | lines that do not express PDE7B (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without PDE7B | 0.024 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent; co-absent with the target |
| [[BMPER]] | C | PDE7B activity raises BMPER's level | lines that do not express PDE7B (26) vs lines expressing it (24) | 2.60× lower at baseline in the lines without PDE7B | 0.024 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent; co-absent with the target |
| [[PDE4B]] | C | PDE7B activity raises PDE4B's level | lines that do not express PDE7B (26) vs lines expressing it (24) | 3.39× lower at baseline in the lines without PDE7B | 0.053 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent; co-absent with the target |
| [[TCF4]] | C | PDE7B activity raises TCF4's level | lines that do not express PDE7B (26) vs lines expressing it (24) | 4.63× lower at baseline in the lines without PDE7B | 0.057 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent; co-absent with the target |
| [[KCNE4]] | C | PDE7B activity raises KCNE4's level | lines that do not express PDE7B (26) vs lines expressing it (24) | 2.79× lower at baseline in the lines without PDE7B | 0.064 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent; co-absent with the target |
| [[FENDRR]] | C | PDE7B activity raises FENDRR's level | lines that do not express PDE7B (26) vs lines expressing it (24) | 2.66× lower at baseline in the lines without PDE7B | 0.072 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent; co-absent with the target |
| [[SGIP1]] | C | PDE7B activity raises SGIP1's level | lines that do not express PDE7B (26) vs lines expressing it (24) | 3.30× lower at baseline in the lines without PDE7B | 0.079 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent; co-absent with the target |
| [[C5orf46]] | C | PDE7B activity raises C5orf46's level | lines that do not express PDE7B (26) vs lines expressing it (24) | 1.57× lower at baseline in the lines without PDE7B | 0.079 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.2, 34.6); signed map (41.8, 43.2). **Vector** length 74.4, 22.5% of its response variance represented; |z| ≥ 3 in 659 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 7B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:135,851,701-136,195,574 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphodiesterases |
| Reactome | 3 pathways, smallest: G alpha (s) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP56](https://www.uniprot.org/uniprotkb/Q9NP56) (3',5'-cyclic-AMP phosphodiesterase 7B):

> Hydrolyzes the second messenger cAMP, which is a key regulator of many important physiological processes. May be involved in the control of cAMP-mediated neural activity and cAMP metabolism in the brain.

**Summary**, from NCBI Gene [27115](https://www.ncbi.nlm.nih.gov/gene/27115):

> The 3',5'-cyclic nucleotides cAMP and cGMP function as second messengers in a wide variety of signal transduction pathways. 3',5'-cyclic nucleotide phosphodiesterases (PDEs) catalyze the hydrolysis of cAMP and cGMP to the corresponding 5'-monophosphates and provide a mechanism to downregulate cAMP and cGMP signaling. This gene encodes a cAMP-specific phosphodiesterase, a member of the cyclic nucleotide phosphodiesterase family.[provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:8792](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8792) · Entrez [27115](https://www.ncbi.nlm.nih.gov/gene/27115) · UniProt [Q9NP56](https://www.uniprot.org/uniprotkb/Q9NP56) · Ensembl [ENSG00000171408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171408)

## Data

Gene col 10101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10101); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10101]; `tensor/DDL_lfc|DDL_z.npy` [10101]; `embed/gene_vectors.npy` [10101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10101 or target_col == 10101). Every well: [[PDE7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
