---
symbol: "GSDMC"
type: "gene"
col: 7219
ensembl_id: "ENSG00000147697"
name: "gasdermin C"
location: "8q24.21"
module: 155
arm: "+"
pooled_cpm: 3.38
n_lines_expressing: 8
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 21
direction_downstream: 45
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# GSDMC

*gasdermin C* — 8q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.28× (z +10.9, q 4e-25, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.60× (z +8.4, q 2e-14, up in 0 of 6 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.495× (z -4.2, q 0.014, down in 5 of 6 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[S100A9]] (+0.87, fdr 7e-06), [[S100A8]] (+0.82, fdr 7e-06), [[CES1]] (+0.79, fdr 7e-06); moves opposite to [[PGR]] (-0.48, fdr 3e-05), [[ANKRD30A]] (-0.47, fdr 1e-04), [[LINC00993]] (-0.38, fdr 2e-04).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[CEACAM6]] → it (grade C ⚠); 45 go from it, the strongest it → [[AQP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7219.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.28×** | +10.9 | 4e-25 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +8.4 | 2e-14 | 0/6 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.78×** | +8.2 | 4e-14 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.26×** | +7.9 | 3e-13 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.07×** | +5.0 | 8e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.89×** | +4.4 | 0.001 | 0/2 | top dose only | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +4.1 | 0.003 | 0/6 | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.003 | 0/6 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.003 | 4/6 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +3.9 | 0.006 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.9 | 0.006 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.99×** | +3.5 | 0.018 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.018 | 0/6 | top dose only | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +3.4 | 0.023 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.15×** | +3.4 | 0.027 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.66×** | +3.1 | 0.061 | 2/6 (NCI-H1573, NCI-H2347) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.62×** | +3.0 | 0.092 | 2/6 (NCI-H1573, NCI-H2347) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7219.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.495×** | -4.2 | 0.014 | 5/6 (BT-474, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.524×** | -3.6 | 0.087 | 4/6 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.570×** | -3.5 | 0.087 | 0/6 | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.593× | -3.3 | 0.14 | 5/6 (BT-474, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.600× | -3.2 | 0.14 | 0/6 | inconsistent across doses |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.600× | -3.2 | 0.14 | 0/6 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7219. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 25.4 | 0 | 21 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0101× (z -26.8) |
| [[Hs 766T (line)]] | wt | 60.8 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0262× (z -21.4) |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0168× (z -22.6) |
| [[CFPAC-1 (line)]] | alt | 35.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0520× (z -21.6) |
| [[A-172 (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.266 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.382 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.821 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.340 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.275 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7219), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[S100A9]] | +0.87 | +0.79 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[S100A8]] | +0.82 | +0.79 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[CES1]] | +0.79 | +0.75 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB3]] | +0.75 | +0.73 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB4]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[FGB]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[FAM83A]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[P2RY2]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[SERPINA1]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[LINC01440]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[FLRT3]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[GPR141]] | +0.61 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGR]] | -0.48 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ANKRD30A]] | -0.47 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[LINC00993]] | -0.38 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[PRLR]] | -0.37 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[LONRF2]] | -0.37 | -0.41 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 0, C 21. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEACAM6]] | C | CEACAM6 activity raises GSDMC's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 3.26× lower at baseline in the lines without CEACAM6 | 0.012 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[FAM83A]] | C | FAM83A activity raises GSDMC's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 3.44× lower at baseline in the lines without FAM83A | 0.014 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9; co-absent with the target |
| [[KRT7]] | C | KRT7 activity raises GSDMC's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 2.71× lower at baseline in the lines without KRT7 | 0.017 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3; co-absent with the target |
| [[C2CD4A]] | C | C2CD4A activity raises GSDMC's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 2.27× lower at baseline in the lines without C2CD4A | 0.019 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L; co-absent with the target |
| [[S100P]] | C | S100P activity raises GSDMC's level | lines that do not express S100P (34) vs lines expressing it (16) | 2.46× lower at baseline in the lines without S100P | 0.021 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6; co-absent with the target |
| [[SPTSSB]] | C | SPTSSB activity raises GSDMC's level | lines that do not express SPTSSB (37) vs lines expressing it (13) | 2.15× lower at baseline in the lines without SPTSSB | 0.022 | ⚠ within organs, on part of the lines; also absent: PRR15L, HEPHL1, TACSTD2; co-absent with the target |
| [[P2RY2]] | C | P2RY2 activity raises GSDMC's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.06× lower at baseline in the lines without P2RY2 | 0.028 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; co-absent with the target |
| [[KRT6A]] | C | KRT6A activity raises GSDMC's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 2.45× lower at baseline in the lines without KRT6A | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[SLPI]] | C | SLPI activity raises GSDMC's level | lines that do not express SLPI (25) vs lines expressing it (25) | 1.88× lower at baseline in the lines without SLPI | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2; co-absent with the target |
| [[MUC5AC]] | C | MUC5AC activity raises GSDMC's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 3.14× lower at baseline in the lines without MUC5AC | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3; co-absent with the target |
| [[SLC6A14]] | C | SLC6A14 activity raises GSDMC's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 2.74× lower at baseline in the lines without SLC6A14 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1; co-absent with the target |
| [[ST8SIA6]] | C | ST8SIA6 activity raises GSDMC's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 2.30× lower at baseline in the lines without ST8SIA6 | 0.056 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2; co-absent with the target |

### Downstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 14, C 31. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AQP3]] | B | GSDMC activity raises AQP3's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 3.55× lower at baseline in the lines without GSDMC | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[IQANK1]] | B | GSDMC activity raises IQANK1's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 3.15× lower at baseline in the lines without GSDMC | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[KLF5]] | B | GSDMC activity raises KLF5's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 3.20× lower at baseline in the lines without GSDMC | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[KRT86]] | B | GSDMC activity raises KRT86's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 4.28× lower at baseline in the lines without GSDMC | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[PKP2]] | B | GSDMC activity raises PKP2's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 2.65× lower at baseline in the lines without GSDMC | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[LYPD5]] | B | GSDMC activity raises LYPD5's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 1.55× lower at baseline in the lines without GSDMC | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[CORO2A]] | B | GSDMC activity raises CORO2A's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 1.96× lower at baseline in the lines without GSDMC | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[PTK6]] | B | GSDMC activity raises PTK6's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 3.01× lower at baseline in the lines without GSDMC | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[LGALS9]] | B | GSDMC activity raises LGALS9's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 2.33× lower at baseline in the lines without GSDMC | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| cells under [[Afatinib (drug)]] 0.5 µM | B | GSDMC activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express GSDMC (42) vs lines expressing it (6) | the lines without GSDMC: 1.19× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[ELMO3]] | B | GSDMC activity raises ELMO3's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 1.66× lower at baseline in the lines without GSDMC | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[HAL]] | B | GSDMC activity raises HAL's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 1.94× lower at baseline in the lines without GSDMC | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.3, 48.4); signed map (54.8, 23.7). **Vector** length 48.2, 24.7% of its response variance represented; |z| ≥ 3 in 261 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MyD88 deficiency (TLR2/4)* (reactome, mean cos +0.74 to 4); *IRAK4 deficiency (TLR2/4)* (reactome, mean cos +0.74 to 4); *Regulation of TLR by endogenous ligand* (reactome, mean cos +0.74 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +8.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +1.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +0.9 | +2.0 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.1 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | gasdermin C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.21 — chr8:129,748,196-129,786,624 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MLZE |
| Gene groups (HGNC) | Gasdermins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYG8](https://www.uniprot.org/uniprotkb/Q9BYG8) (Gasdermin-C):

> [Gasdermin-C]: This form constitutes the precursor of the pore-forming protein: upon cleavage, the released N-terminal moiety (Gasdermin-C, N-terminal) binds to membranes and forms pores, triggering pyroptosis.; [Gasdermin-C, N-terminal]: Pore-forming protein that causes membrane permeabilization and pyroptosis. Produced by the cleavage of gasdermin-C by caspase CASP8 in response to death signals. After cleavage, moves to the plasma membrane where it strongly binds to membrane inner leaflet …

**Summary**, from NCBI Gene [56169](https://www.ncbi.nlm.nih.gov/gene/56169):

> Enables wide pore channel activity. Involved in pyroptotic inflammatory response. Located in cytoplasm. Is active in plasma membrane. Biomarker of lung adenocarcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7151) · Entrez [56169](https://www.ncbi.nlm.nih.gov/gene/56169) · UniProt [Q9BYG8](https://www.uniprot.org/uniprotkb/Q9BYG8) · Ensembl [ENSG00000147697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147697)

## Data

Gene col 7219: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7219); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7219, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7219]; `tensor/DDL_lfc|DDL_z.npy` [7219]; `embed/gene_vectors.npy` [7219]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7219 or target_col == 7219). Every well: [[GSDMC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSDMC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
