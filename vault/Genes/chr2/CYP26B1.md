---
symbol: "CYP26B1"
type: "gene"
col: 29
ensembl_id: "ENSG00000003137"
name: "cytochrome P450 family 26 subfamily B member 1"
location: "2p13.2"
module: 13
arm: "+"
pooled_cpm: 3.86
n_lines_expressing: 27
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CYP26B1

*cytochrome P450 family 26 subfamily B member 1* — 2p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.53× (z +11.8, q 2e-29, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.53× (z +10.7, q 5e-24, up in 7 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.627× (z -3.8, q 0.072, down in 10 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.0458×, RPMI-7951 0.132×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.139×, RPMI-7951 0.164×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.0887×, HS-578T 0.0808×; ⚠ cell-cycle shift, explains ~26% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0693×); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0779×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRTAC1]] (+0.68, fdr 1e-05), [[VSTM4]] (+0.60, fdr 1e-05), [[TMOD1]] (+0.58, fdr 3e-05); moves opposite to [[NPRL3]] (-0.44, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KALRN]] → it (grade B ⚠); 2 go from it, the strongest it → [[TTYH2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 29.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.53×** | +11.8 | 2e-29 | 1/5 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +10.7 | 5e-24 | 7/14 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +8.3 | 2e-14 | 4/9 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +7.9 | 6e-13 | 11/22 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.75×** | +7.6 | 3e-12 | 1/6 (RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +5.6 | 2e-06 | 8/24 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.94×** | +5.4 | 6e-06 | 8/24 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +4.7 | 1e-04 | 2/10 (LoVo, HEC-1-A) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.78×** | +4.7 | 2e-04 | 8/20 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.46×** | +4.3 | 8e-04 | 10/24 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +4.0 | 0.004 | 8/19 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +3.9 | 0.004 | 1/13 (HEC-1-A) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.008 | 4/24 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +3.5 | 0.017 | 2/6 (LoVo, NCI-H2030) | top dose only | noisy plate (z scaled) |
| [[Tazarotene (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.017 | 8/23 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.53×** | +3.5 | 0.019 | 8/24 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.51×** | +3.1 | 0.064 | 2/13 (HEC-1-A, NCI-H2030) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.1 | 0.064 | 0/15 | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Roxadustat (drug)]] 0.05 µM |  | **1.49×** | +3.0 | 0.081 | 1/16 (LoVo) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 29.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.0458×, RPMI-7951 0.132×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.139×, RPMI-7951 0.164×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.0887×, HS-578T 0.0808×; ⚠ cell-cycle shift, explains ~26% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0693×); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0779×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.627×** | -3.8 | 0.072 | 10/22 (NCI-H23, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 29. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 67.2 | 2 | 13 (9 ⚠) | [[Retinoic acid (drug)]] 5 µM 3.88× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.0458× (z -23.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -15.3) |
| [[RPMI-7951 (line)]] | alt | 15.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -8.6) |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0808× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.843 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.898 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.700 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.724 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.425 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 29), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTAC1]] | +0.68 | +0.49 / +0.75 | both halves | 1e-05 |  |
| [[VSTM4]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[TMOD1]] | +0.58 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[IL1B]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[GSDME]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[AADACP1]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ANXA10]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PTGS2]] | +0.55 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[GJA1]] | +0.53 | +0.42 / +0.49 | both halves | 4e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[NTF3]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[LINC01411]] | +0.53 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[TRPA1]] | +0.53 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPRL3]] | -0.44 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KALRN]] | B | KALRN activity lowers CYP26B1's level | lines that do not express KALRN (10) vs lines expressing it (40) | 1.39× higher at baseline in the lines without KALRN | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HTRA3]] | B | HTRA3 activity raises CYP26B1's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 1.88× lower at baseline in the lines without HTRA3 | 0.054 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[IL33]] | B | IL33 activity raises CYP26B1's level | lines that do not express IL33 (35) vs lines expressing it (15) | 1.63× lower at baseline in the lines without IL33 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411 |
| [[GJA1]] | B | GJA1 activity raises CYP26B1's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 2.00× lower at baseline in the lines without GJA1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTYH2]] | B | CYP26B1 activity raises TTYH2's level | lines that do not express CYP26B1 (23) vs lines expressing it (27) | 1.72× lower at baseline in the lines without CYP26B1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, ENSG00000242029, ELOVL2 |
| [[GJA1]] | B | CYP26B1 activity raises GJA1's level | lines that do not express CYP26B1 (23) vs lines expressing it (27) | 2.36× lower at baseline in the lines without CYP26B1 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, ENSG00000242029, ELOVL2 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.6, 17.4); signed map (22.8, 51.6). **Vector** length 46.7, 8.70% of its response variance represented; |z| ≥ 3 in 714 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +1.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 26 subfamily B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.2 — chr2:72,129,238-72,147,862 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P450RAI-2 |
| Gene groups (HGNC) | Cytochrome P450 family 26 |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 9 pathways, smallest: Vitamins; RA biosynthesis pathway; Metabolic disorders of biological oxidation enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR63](https://www.uniprot.org/uniprotkb/Q9NR63) (Cytochrome P450 26B1):

> A cytochrome P450 monooxygenase involved in the metabolism of retinoates (RAs), the active metabolites of vitamin A, and critical signaling molecules in animals. RAs exist as at least four different isomers: all-trans-RA (atRA), 9-cis-RA, 13-cis-RA, and 9,13-dicis-RA, where atRA is considered to be the biologically active isomer, although 9-cis-RA and 13-cis-RA also have activity (Probable). Catalyzes the hydroxylation of atRA primarily at C-4 and C-18, thereby contributing to the regulation of …

**Summary**, from NCBI Gene [56603](https://www.ncbi.nlm.nih.gov/gene/56603):

> This gene encodes a member of the cytochrome P450 superfamily. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. The encoded protein is localized to the endoplasmic reticulum, and functions as a critical regulator of all-trans retinoic acid levels by the specific inactivation of all-trans retinoic acid to hydroxylated forms. Mutations in this gene are associated with radiohumeral …

**Accessions** — [HGNC:20581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20581) · Entrez [56603](https://www.ncbi.nlm.nih.gov/gene/56603) · UniProt [Q9NR63](https://www.uniprot.org/uniprotkb/Q9NR63) · Ensembl [ENSG00000003137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000003137)

## Data

Gene col 29: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 29); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 29, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 29]; `tensor/DDL_lfc|DDL_z.npy` [29]; `embed/gene_vectors.npy` [29]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 29 or target_col == 29). Every well: [[CYP26B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP26B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
