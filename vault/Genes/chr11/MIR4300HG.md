---
symbol: "MIR4300HG"
type: "gene"
col: 14445
ensembl_id: "ENSG00000245832"
name: "MIR4300 host gene"
location: "11q14.1"
module: 75
arm: "+"
pooled_cpm: 3.05
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 1
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# MIR4300HG

*MIR4300 host gene* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.75× (z +29.5, q 0e+00, up in 32 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Balsalazide (sodium hydrate) (drug)]] 5 µM: 0.744× (z -4.0, q 0.042, down in 9 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Monocrotaline (drug)]] 5 µM in 1 line (NCI-H460 0.0594×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC4C]] (+0.88, fdr 7e-06), [[SCHLAP1]] (+0.84, fdr 7e-06), [[DPP6]] (+0.83, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LINC00958]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.75×** | +29.5 | 0e+00 | 32/33 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **7.72×** | +27.8 | 0e+00 | 31/32 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.26×** | +13.9 | 7e-42 | 32/38 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.03×** | +13.4 | 8e-39 | 11/12 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.97×** | +13.3 | 4e-38 | 35/41 (LOX-IMVI, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.89×** | +12.6 | 4e-34 | 3/4 (HS-578T, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.78×** | +11.8 | 2e-30 | 3/5 (SK-MEL-2, A498, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.35×** | +11.6 | 2e-29 | 26/33 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.27×** | +11.2 | 4e-27 | 33/44 (SW480, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.70×** | +9.2 | 2e-18 | 22/40 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.89×** | +8.6 | 3e-16 | 17/43 (PANC-1, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +8.0 | 5e-14 | 18/36 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +6.7 | 1e-09 | 13/29 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +6.4 | 7e-09 | 12/27 (LOX-IMVI, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +5.9 | 1e-07 | 20/45 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +5.9 | 1e-07 | 18/39 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +5.2 | 8e-06 | 15/44 (SW1417, NCI-H23, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +4.8 | 4e-05 | 15/43 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.002 | 3/35 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14445.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Monocrotaline (drug)]] 5 µM in 1 line (NCI-H460 0.0594×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | **0.744×** | -4.0 | 0.042 | 9/45 (CFPAC-1, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -3.7 | 0.071 | 17/47 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.18 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.0× (z +17.2) | — |
| [[NCI-H460 (line)]] | wt | 1.86 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +10.8) | [[Monocrotaline (drug)]] 5 µM 0.0594× (z -8.6) |
| [[SW480 (line)]] | alt | 1.96 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.6× (z +14.6) | — |
| [[A498 (line)]] | wt | 2.52 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +11.4) | — |
| [[C32 (line)]] | wt | 2.48 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.0× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 2.01 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 32.5× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 1.90 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +11.9) | — |
| [[J82 (line)]] | alt | 2.17 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +9.9) | — |
| [[KATO III (line)]] | alt | 2.65 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.3× (z +12.2) | — |
| [[LoVo (line)]] | wt | 1.85 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 28.2× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 1.96 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +12.4) | — |
| [[PANC-1 (line)]] | alt | 1.53 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +13.2) | — |
| [[A549 (line)]] | wt | 1.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.5× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 2.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 5.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.71× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 1.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 1.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +11.8) | — |
| [[A-427 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC4C]] | +0.88 | +0.82 / +0.86 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.84 | +0.81 / +0.84 | both halves | 7e-06 |  |
| [[DPP6]] | +0.83 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[USH2A]] | +0.83 | +0.83 / +0.82 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.82 | +0.81 / +0.84 | both halves | 7e-06 |  |
| [[LINC01033]] | +0.82 | +0.78 / +0.78 | both halves | 7e-06 |  |
| [[KCNAB1]] | +0.82 | +0.82 / +0.79 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.81 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.81 | +0.78 / +0.79 | both halves | 7e-06 |  |
| [[DPYD-AS1]] | +0.80 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[SLC9C1]] | +0.80 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[RBMS3-AS3]] | +0.79 | +0.84 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00958]] | B | LINC00958 activity raises MIR4300HG's level | lines that do not express LINC00958 (39) vs lines expressing it (11) | 1.43× lower at baseline in the lines without LINC00958 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SSX1, LINC01320, LINC00879 |
| [[LINC02241]] | B | LINC02241 activity raises MIR4300HG's level | lines that do not express LINC02241 (34) vs lines expressing it (16) | 1.81× lower at baseline in the lines without LINC02241 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000259560, LINC02616, LINC02476; maybe low, not absent |
| [[LY96]] | B | LY96 activity raises MIR4300HG's level | lines that do not express LY96 (18) vs lines expressing it (32) | 1.53× lower at baseline in the lines without LY96 | 0.044 | ⚠ within organs, on part of the lines; also absent: SOX5, ENSG00000287100, ENSG00000287622; maybe low, not absent |
| [[LINC01828]] | B | LINC01828 activity raises MIR4300HG's level | lines that do not express LINC01828 (17) vs lines expressing it (33) | 1.52× lower at baseline in the lines without LINC01828 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, ENSG00000230647, ENSG00000253891; maybe low, not absent |
| [[RALYL]] | B | RALYL activity raises MIR4300HG's level | lines that do not express RALYL (17) vs lines expressing it (33) | 1.46× lower at baseline in the lines without RALYL | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MIR4300HG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ADAMTSL1]] | B | ADAMTSL1 activity raises MIR4300HG's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without ADAMTSL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent |
| [[NRXN1]] | B | NRXN1 activity raises MIR4300HG's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without NRXN1 | 0.074 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[PSG4]] | B | PSG4 activity raises MIR4300HG's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 1.57× lower at baseline in the lines without PSG4 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5 |
| [[SOX11]] | B | SOX11 activity raises MIR4300HG's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 1.57× lower at baseline in the lines without SOX11 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.898). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.3, 28.1); signed map (31.8, 14.2). **Vector** length 61.2, 9.38% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +29.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +27.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +13.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +8.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +4.0 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.6 | +5.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | MIR4300 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q14.1 — chr11:81,821,272-82,718,299 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52003](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52003) · Entrez [101928989](https://www.ncbi.nlm.nih.gov/gene/101928989) · Ensembl [ENSG00000245832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245832)

## Data

Gene col 14445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14445); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14445]; `tensor/DDL_lfc|DDL_z.npy` [14445]; `embed/gene_vectors.npy` [14445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14445 or target_col == 14445). Every well: [[MIR4300HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR4300HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
