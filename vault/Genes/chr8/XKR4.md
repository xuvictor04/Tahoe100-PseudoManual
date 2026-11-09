---
symbol: "XKR4"
type: "gene"
col: 13054
ensembl_id: "ENSG00000206579"
name: "XK related 4"
location: "8q12.1"
module: 61
arm: "+"
pooled_cpm: 2.17
n_lines_expressing: 50
n_dd_up: 47
n_dd_down: 1
n_dd_up_clean: 34
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# XKR4

*XK related 4* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 10.8× (z +28.7, q 0e+00, up in 26 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.631× (z -3.9, q 0.046, down in 5 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGCZ]] (+0.82, fdr 7e-06), [[GRIA4]] (+0.81, fdr 7e-06), [[DLGAP2]] (+0.81, fdr 7e-06).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[STX11]] → it (grade B ⚠); 2 go from it, the strongest it → [[CLVS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13054.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **10.8×** | +28.7 | 0e+00 | 26/26 (SW48, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.22×** | +22.0 | 0e+00 | 19/20 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.73×** | +14.9 | 0e+00 | 5/7 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.35×** | +13.7 | 9e-41 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.13×** | +13.7 | 9e-41 | 27/40 (NCI-H2030, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.38×** | +12.6 | 3e-34 | 14/22 (SHP-77, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.50×** | +11.3 | 9e-28 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **3.45×** | +10.1 | 3e-22 | 20/31 (SW48, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.85×** | +8.9 | 3e-17 | 21/34 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.16×** | +6.6 | 3e-09 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.4 | 6e-09 | 4/39 (PANC-1, A549, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.12×** | +6.4 | 9e-09 | 13/26 (C32, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +5.5 | 2e-06 | 12/26 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.2 | 8e-06 | 2/10 (NCI-H2347, A-427) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.19×** | +5.2 | 1e-05 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +5.1 | 1e-05 | 4/14 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +5.1 | 1e-05 | 7/25 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +4.5 | 2e-04 | 17/43 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.42×** | +4.2 | 8e-04 | 0/18 | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.003 | 6/35 (SHP-77, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.57×** | +3.8 | 0.003 | 4/34 (A-427, SHP-77, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13054.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.631×** | -3.9 | 0.046 | 5/37 (LOX-IMVI, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13054. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 1.82 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 27.6× (z +10.2) | — |
| [[C32 (line)]] | wt | 1.14 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 26.1× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 0.840 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.6× (z +13.7) | — |
| [[A549 (line)]] | wt | 1.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.4× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 0.931 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.5× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 0.928 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +9.6) | — |
| [[HepG2_C3A (line)]] | wt | 1.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 53.0× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 0.942 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 1.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.0× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 1.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.3× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 1.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 47.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 5.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +10.1) | — |
| [[SW48 (line)]] | wt | 1.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 403× (z +14.2) | — |
| [[SW480 (line)]] | alt | 2.00 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.77× (z +9.0) | — |
| [[A-172 (line)]] | wt | 0.831 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.775 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.822 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.975 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.840 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.994 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.936 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.877 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.925 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.778 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.858 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.795 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.869 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.720 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.751 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.838 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.938 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.852 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.955 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13054), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGCZ]] | +0.82 | +0.79 / +0.85 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.81 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.81 | +0.83 / +0.77 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.78 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[SLC35F1]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[LINC02511]] | +0.77 | +0.76 / +0.80 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[DNAH3]] | +0.75 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[SLC9C1]] | +0.75 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[LUZP2]] | +0.75 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.75 | +0.73 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STX11]] | B | STX11 activity lowers XKR4's level | lines that do not express STX11 (8) vs lines expressing it (42) | 1.75× higher at baseline in the lines without STX11 | 0.005 | ⚠ within organs, on part of the lines; also absent: TSPAN4 |
| [[SLC7A11-AS1]] | B | SLC7A11-AS1 activity lowers XKR4's level | lines that do not express SLC7A11-AS1 (11) vs lines expressing it (39) | 1.39× higher at baseline in the lines without SLC7A11-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers XKR4's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 10.1% of all compounds | 0.022 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[KCND2]] | B | KCND2 activity raises XKR4's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.38× lower at baseline in the lines without KCND2 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent |
| [[MCOLN3]] | B | MCOLN3 activity lowers XKR4's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 1.12× higher at baseline in the lines without MCOLN3 | 0.096 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |
| [[DUSP8]] | C | DUSP8 activity lowers XKR4's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 1.90× higher at baseline in the lines without DUSP8 | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLVS1]] | C | XKR4's natural level weakens CLVS1's drug response | XKR4's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.27; direction clear | 0.020 | ⚠ tissue can mimic it; precision caveat |
| [[SEMA6D]] | C | XKR4's natural level weakens SEMA6D's drug response | XKR4's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.17; direction not clear | 0.0995 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.803). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.8, 29.7); signed map (32.2, 16.3). **Vector** length 49.1, 7.54% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +28.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +13.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +22.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +6.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | -0.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -3.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | XK related 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:55,102,028-55,542,054 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1889 |
| Gene groups (HGNC) | XK related family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5GH76](https://www.uniprot.org/uniprotkb/Q5GH76) (XK-related protein 4):

> [XK-related protein 4, processed form]: Phospholipid scramblase that promotes phosphatidylserine exposure on apoptotic cell surface. Phosphatidylserine is a specific marker only present at the surface of apoptotic cells and acts as a specific signal for engulfment.

**Summary**, from NCBI Gene [114786](https://www.ncbi.nlm.nih.gov/gene/114786):

> Enables phospholipid scramblase activity. Involved in phosphatidylserine exposure on apoptotic cell surface. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29394](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29394) · Entrez [114786](https://www.ncbi.nlm.nih.gov/gene/114786) · UniProt [Q5GH76](https://www.uniprot.org/uniprotkb/Q5GH76) · Ensembl [ENSG00000206579](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206579)

## Data

Gene col 13054: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13054); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13054, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13054]; `tensor/DDL_lfc|DDL_z.npy` [13054]; `embed/gene_vectors.npy` [13054]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13054 or target_col == 13054). Every well: [[XKR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XKR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
