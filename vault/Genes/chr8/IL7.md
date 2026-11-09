---
symbol: "IL7"
type: "gene"
col: 2461
ensembl_id: "ENSG00000104432"
name: "interleukin 7"
location: "8q21.13"
module: 70
arm: "+"
pooled_cpm: 20.38
n_lines_expressing: 43
n_dd_up: 4
n_dd_down: 25
n_dd_up_clean: 4
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 7
direction_downstream: 10
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# IL7

*interleukin 7* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.83× (z +9.0, q 2e-16, up in 25 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.523× (z -9.6, q 3e-19, down in 26 of 41 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKIA-AS1]] (+0.60, fdr 1e-05), [[PLSCR4]] (+0.52, fdr 7e-05), [[BTN3A1]] (+0.48, fdr 2e-05); moves opposite to [[PSKH1]] (-0.42, fdr 5e-05), [[ZNF76]] (-0.39, fdr 2e-04), [[KLHL12]] (-0.38, fdr 3e-04).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[IFI16]] → it (grade B ⚠); 10 go from it, the strongest it → [[PLSCR4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2461.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +9.0 | 2e-16 | 25/41 (RKO, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +8.8 | 6e-16 | 23/41 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +5.2 | 5e-05 | 18/40 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 6e-04 | 18/41 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.18× | +3.4 | 0.064 | 16/40 (HOP62, NCI-H460, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | 1.50× | +3.2 | 0.14 | 5/40 (RKO, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.25× | +3.1 | 0.14 | 5/40 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 5 µM |  | 1.16× | +3.1 | 0.14 | 4/41 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.0 | 0.14 | 8/41 (AsPC-1, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2461.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.523×** | -9.6 | 3e-19 | 26/41 (H4, SW 1271, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.743×** | -6.3 | 1e-07 | 22/41 (RKO, H4, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.668×** | -6.0 | 4e-07 | 21/41 (LoVo, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.684×** | -5.6 | 2e-06 | 17/41 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.696×** | -5.4 | 8e-06 | 19/41 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.697×** | -5.4 | 8e-06 | 21/40 (SW48, RKO, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.700×** | -5.3 | 9e-06 | 21/40 (A498, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.723×** | -4.8 | 1e-04 | 20/40 (A498, RKO, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.726×** | -4.8 | 1e-04 | 21/41 (RKO, CFPAC-1, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.742×** | -4.4 | 7e-04 | 16/41 (H4, CFPAC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -4.3 | 9e-04 | 5/41 (HCT15, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.764×** | -4.0 | 0.003 | 15/40 (SW48, BT-474, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.766×** | -4.0 | 0.003 | 15/40 (RKO, H4, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.777×** | -3.6 | 0.012 | 16/40 (RKO, SNU-423, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.778×** | -3.6 | 0.012 | 8/41 (A498, Panc 03.27, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.786×** | -3.6 | 0.012 | 14/41 (RKO, C32, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.633×** | -3.6 | 0.012 | 8/41 (PANC-1, H4, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.634×** | -3.5 | 0.012 | 14/36 (RPMI-7951, H4, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.641×** | -3.5 | 0.017 | 12/40 (SHP-77, A498, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2461. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 81.5 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.228× (z -13.0) |
| [[HS-578T (line)]] | alt | 35.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +23.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 80.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CHP-212 (line)]] | wt | 42.5 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0759× (z -9.8) |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0961× (z -8.5) |
| [[H4 (line)]] | wt | 45.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.173× (z -9.4) |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.120× (z -9.7) |
| [[HOP62 (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +17.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.67× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 27.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 47.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 30.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -8.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[LS 180 (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.216× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 5.88 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.01× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 11.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.65 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2461), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKIA-AS1]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[PLSCR4]] | +0.52 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[BTN3A1]] | +0.48 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[BTN3A2]] | +0.47 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[CFH]] | +0.47 | +0.50 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[HERC5]] | +0.47 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[IFI44]] | +0.46 | +0.47 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[GBP4]] | +0.46 | +0.39 / +0.49 | both halves | 6e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TNIP3]] | +0.46 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[MAML2]] | +0.46 | +0.43 / +0.36 | both halves | 1e-04 |  |
| [[CYP2J2]] | +0.46 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[VCAM1]] | +0.45 | +0.41 / +0.46 | both halves | 4e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 563 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSKH1]] | -0.42 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[ZNF76]] | -0.39 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[KLHL12]] | -0.38 | -0.36 / -0.29 | both halves | 3e-04 |  |
| [[TMEM250]] | -0.37 | -0.28 / -0.31 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI16]] | B | IFI16 activity raises IL7's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.50× lower at baseline in the lines without IFI16 | 0.001 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[SLFN12]] | B | SLFN12 activity raises IL7's level | lines that do not express SLFN12 (22) vs lines expressing it (28) | 1.97× lower at baseline in the lines without SLFN12 | 0.007 | ⚠ within organs, on part of the lines; also absent: LAMA4, CHSY3, NLRP1 |
| [[GBP3]] | B | GBP3 activity raises IL7's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 2.51× lower at baseline in the lines without GBP3 | 0.015 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[VDR]] | B | VDR activity raises IL7's level | lines that do not express VDR (8) vs lines expressing it (42) | 2.83× lower at baseline in the lines without VDR | 0.017 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers IL7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[MX1]] | B | MX1 activity raises IL7's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.89× lower at baseline in the lines without MX1 | 0.055 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[FYB1]] | B | FYB1 activity raises IL7's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 1.68× lower at baseline in the lines without FYB1 | 0.062 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLSCR4]] | B | IL7 activity raises PLSCR4's level | lines that do not express IL7 (7) vs lines expressing it (43) | 4.61× lower at baseline in the lines without IL7 | 0.005 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent |
| [[MAP3K5]] | B | IL7 activity raises MAP3K5's level | lines that do not express IL7 (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without IL7 | 0.012 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent |
| [[IL15]] | B | IL7 activity raises IL15's level | lines that do not express IL7 (7) vs lines expressing it (43) | 3.82× lower at baseline in the lines without IL7 | 0.019 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent |
| [[ALPK1]] | B | IL7 activity raises ALPK1's level | lines that do not express IL7 (7) vs lines expressing it (43) | 2.89× lower at baseline in the lines without IL7 | 0.034 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent |
| [[GBP3]] | B | IL7 activity raises GBP3's level | lines that do not express IL7 (7) vs lines expressing it (43) | 3.18× lower at baseline in the lines without IL7 | 0.055 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | IL7 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express IL7 (7) vs lines expressing it (41) | the lines without IL7: 0.80× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent |
| [[IFI44]] | B | IL7 activity raises IFI44's level | lines that do not express IL7 (7) vs lines expressing it (43) | 3.86× lower at baseline in the lines without IL7 | 0.088 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent |
| [[GBP4]] | B | IL7 activity raises GBP4's level | lines that do not express IL7 (7) vs lines expressing it (43) | 3.55× lower at baseline in the lines without IL7 | 0.090 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent |
| [[CRYBG1]] | B | IL7 activity raises CRYBG1's level | lines that do not express IL7 (7) vs lines expressing it (43) | 3.77× lower at baseline in the lines without IL7 | 0.0998 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent |
| [[ATP1B1]] | C | IL7 activity raises ATP1B1's level | lines that do not express IL7 (7) vs lines expressing it (43) | 3.49× lower at baseline in the lines without IL7 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.410). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.2, 52.3); signed map (58.2, 29.5). **Vector** length 84.5, 16.7% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.1 | +3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.8 | +9.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Regorafenib (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +5.2 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.5 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.1 | -9.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -6.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.3 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -6.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:78,675,743-78,805,523 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IL-7 |
| Gene groups (HGNC) | Interleukins; Interleukin 2 family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INTERFERON_ALPHA_RESPONSE, ALLOGRAFT_REJECTION, INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: Interleukin-7 signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [P13232](https://www.uniprot.org/uniprotkb/P13232) (Interleukin-7):

> Hematopoietic cytokine that plays an essential role in the development, expansion, and survival of naive and memory T-cells and B-cells thereby regulating the number of mature lymphocytes and maintaining lymphoid homeostasis. Mechanistically, exerts its biological effects through a receptor composed of IL7RA subunit and the cytokine receptor common subunit gamma/CSF2RG. Binding to the receptor leads to activation of various kinases including JAK1 or JAK3 depending on the cell type and …

**Summary**, from NCBI Gene [3574](https://www.ncbi.nlm.nih.gov/gene/3574):

> The protein encoded by this gene is a cytokine important for B and T cell development. This cytokine and the hepatocyte growth factor (HGF) form a heterodimer that functions as a pre-pro-B cell growth-stimulating factor. IL7 is found to be a cofactor for V(D)J rearrangement of the T cell receptor beta (TCRB) during early T cell development. This cytokine can be produced locally by intestinal epithelial and epithelial goblet cells, and may serve as a regulatory factor for intestinal mucosal …

**Accessions** — [HGNC:6023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6023) · Entrez [3574](https://www.ncbi.nlm.nih.gov/gene/3574) · UniProt [P13232](https://www.uniprot.org/uniprotkb/P13232) · Ensembl [ENSG00000104432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104432)

## Data

Gene col 2461: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2461); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2461, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2461]; `tensor/DDL_lfc|DDL_z.npy` [2461]; `embed/gene_vectors.npy` [2461]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2461 or target_col == 2461). Every well: [[IL7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
