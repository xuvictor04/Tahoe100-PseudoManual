---
symbol: "TG"
type: "gene"
col: 490
ensembl_id: "ENSG00000042832"
name: "thyroglobulin"
location: "8q24.22"
module: 53
arm: "+"
pooled_cpm: 2.24
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# TG

*thyroglobulin* — 8q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 14.6× (z +26.1, q 0e+00, up in 29 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEB]] (+0.80, fdr 7e-06), [[PKD1L1]] (+0.79, fdr 7e-06), [[H2AZ1-DT]] (+0.78, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **14.6×** | +26.1 | 0e+00 | 29/29 (NCI-H23, HT-29, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **7.90×** | +20.1 | 0e+00 | 27/31 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **7.47×** | +13.3 | 4e-38 | 20/24 (LOX-IMVI, A498, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.91×** | +13.3 | 4e-38 | 24/29 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **6.17×** | +12.0 | 2e-31 | 23/31 (HT-29, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **5.24×** | +11.4 | 5e-28 | 25/36 (HT-29, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.92×** | +9.0 | 1e-17 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.05×** | +8.9 | 4e-17 | 2/4 (A498, HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.45×** | +8.7 | 2e-16 | 22/40 (A498, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +6.8 | 5e-10 | 22/40 (LS 180, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.52×** | +6.3 | 1e-08 | 27/45 (A498, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +6.3 | 2e-08 | 4/14 (BT-474, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.44×** | +6.1 | 4e-08 | 23/37 (BT-474, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +5.4 | 3e-06 | 6/14 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.12×** | +5.2 | 1e-05 | 13/33 (LS 180, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.75×** | +3.8 | 0.004 | 8/43 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.78×** | +3.7 | 0.006 | 6/37 (A549, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +3.5 | 0.012 | 9/40 (BT-474, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.60×** | +3.2 | 0.036 | 8/38 (NCI-H460, RKO, …) | all doses, flat |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 3.04 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.0× (z +10.2) | — |
| [[LoVo (line)]] | wt | 1.58 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.7× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 4.28 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 1.56 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.5× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 1.08 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.8× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 1.38 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +10.3) | — |
| [[A-172 (line)]] | wt | 1.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 27.4× (z +9.0) | — |
| [[A498 (line)]] | wt | 3.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +10.1) | — |
| [[C32 (line)]] | wt | 2.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.0× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 2.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.3× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 1.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.5× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 4.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.6× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 3.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 32.7× (z +11.6) | — |
| [[KATO III (line)]] | alt | 1.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.8× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 3.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 33.5× (z +13.3) | — |
| [[RPMI-7951 (line)]] | alt | 10.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +8.8) | — |
| [[A-427 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.703 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.601 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.886 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.681 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.564 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.696 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.945 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.897 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.962 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEB]] | +0.80 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.79 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[H2AZ1-DT]] | +0.78 | +0.83 / +0.64 | both halves | 7e-06 |  |
| [[C2CD6]] | +0.78 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.78 | +0.80 / +0.63 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.77 | +0.82 / +0.50 | both halves | 1e-05 |  |
| [[IL12RB2]] | +0.77 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[LINC02268]] | +0.76 | +0.80 / +0.62 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.76 | +0.80 / +0.55 | both halves | 1e-05 |  |
| [[LINC00607]] | +0.75 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.75 | +0.78 / +0.58 | both halves | 8e-06 |  |
| [[TMEM202-AS1]] | +0.75 | +0.83 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TG's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[AOX1]] | B | AOX1 activity raises TG's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 1.53× lower at baseline in the lines without AOX1 | 0.022 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[DPYS]] | B | DPYS activity raises TG's level | lines that do not express DPYS (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without DPYS | 0.042 | ⚠ within organs, on part of the lines; also absent: SYNE1, ANGPT1, PCDH9; maybe low, not absent |
| [[RP1]] | B | RP1 activity raises TG's level | lines that do not express RP1 (19) vs lines expressing it (31) | 1.27× lower at baseline in the lines without RP1 | 0.066 | ⚠ within organs, on part of the lines; also absent: CYB5R2, KIAA1549L, KCNN4; maybe low, not absent |
| [[DDR2]] | B | DDR2 activity strengthens TG's drug response | lines that do not express DDR2 (8) vs lines expressing it (34) | the lines without DDR2 respond 0.66× as strongly (z diff +1.06); strongest at Homoharringtonine 5 µM: 3.01x vs 7.82x (z diff +3.2) | 0.076 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MGC4859]] | B | MGC4859 activity raises TG's level | lines that do not express MGC4859 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without MGC4859 | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC00922, LINC01811, LINC00276; maybe low, not absent |
| [[DDR2]] | B | DDR2 activity raises TG's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without DDR2 | 0.090 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[FER1L6]] | B | FER1L6 activity raises TG's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without FER1L6 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[IMPA1P1]] | B | IMPA1P1 activity raises TG's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without IMPA1P1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.4, -9.6); signed map (22.6, 9.1). **Vector** length 71.0, 11.9% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +26.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +20.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +6.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | thyroglobulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.22 — chr8:132,866,958-133,134,903 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TGN, AITD3 |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [P01266](https://www.uniprot.org/uniprotkb/P01266) (Thyroglobulin):

> Acts as a substrate for the production of iodinated thyroid hormones thyroxine (T4) and triiodothyronine (T3). The synthesis of T3 and T4 involves iodination of selected tyrosine residues of TG/thyroglobulin followed by their oxidative coupling in the thyroid follicle lumen. Following TG re-internalization and lysosomal-mediated proteolysis, T3 and T4 are released from the polypeptide backbone leading to their secretion into the bloodstream. One dimer produces 7 thyroid hormone molecules.

**Summary**, from NCBI Gene [7038](https://www.ncbi.nlm.nih.gov/gene/7038):

> Thyroglobulin (Tg) is a glycoprotein homodimer produced predominantly by the thryroid gland. It acts as a substrate for the synthesis of thyroxine and triiodothyronine as well as the storage of the inactive forms of thyroid hormone and iodine. Thyroglobulin is secreted from the endoplasmic reticulum to its site of iodination, and subsequent thyroxine biosynthesis, in the follicular lumen. Mutations in this gene cause thyroid dyshormonogenesis, manifested as goiter, and are associated with …

**Accessions** — [HGNC:11764](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11764) · Entrez [7038](https://www.ncbi.nlm.nih.gov/gene/7038) · UniProt [P01266](https://www.uniprot.org/uniprotkb/P01266) · Ensembl [ENSG00000042832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000042832)

## Data

Gene col 490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 490); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 490]; `tensor/DDL_lfc|DDL_z.npy` [490]; `embed/gene_vectors.npy` [490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 490 or target_col == 490). Every well: [[TG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
