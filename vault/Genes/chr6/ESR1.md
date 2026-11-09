---
symbol: "ESR1"
type: "gene"
col: 1677
ensembl_id: "ENSG00000091831"
name: "estrogen receptor 1"
location: "6q25.1-q25.2"
module: 166
arm: "+"
pooled_cpm: 3.75
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# ESR1

*estrogen receptor 1* — 6q25.1-q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.60× (z +25.4, q 0e+00, up in 26 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (drug)]] 0.05 µM in 1 line (A-172 0.0550×); [[Belinostat (drug)]] 5 µM in 1 line (SK-MEL-2 0.190×; ⚠ cell-cycle shift, explains ~14% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-423 0.121×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OBI1-AS1]] (+0.85, fdr 7e-06), [[SORCS1]] (+0.80, fdr 7e-06), [[LRRC4C]] (+0.79, fdr 7e-06).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[LINC02240]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1677.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.60×** | +25.4 | 0e+00 | 26/31 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.18×** | +21.1 | 0e+00 | 30/33 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.09×** | +14.7 | 0e+00 | 7/16 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.51×** | +13.1 | 5e-37 | 31/38 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.31×** | +12.3 | 9e-33 | 31/43 (SW480, SHP-77, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.19×** | +11.2 | 4e-27 | 2/6 (BT-474, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.84×** | +10.9 | 1e-25 | 20/30 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +10.6 | 1e-24 | 2/6 (HS-578T, BT-474) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.66×** | +10.2 | 2e-22 | 22/40 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.2 | 4e-08 | 7/43 (HEC-1-A, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +6.1 | 6e-08 | 18/37 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +5.8 | 3e-07 | 13/37 (A-172, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.1 | 2e-05 | 11/35 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +5.0 | 3e-05 | 8/38 (A-172, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.61×** | +4.9 | 3e-05 | 5/29 (HOP62, SHP-77, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.3 | 5e-04 | 7/29 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.003 | 16/45 (SHP-77, A-427, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.004 | 3/26 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1677.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (drug)]] 0.05 µM in 1 line (A-172 0.0550×); [[Belinostat (drug)]] 5 µM in 1 line (SK-MEL-2 0.190×; ⚠ cell-cycle shift, explains ~14% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-423 0.121×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.914× | -3.5 | 0.30 | 15/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1677. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.66 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +14.2) | [[Neratinib (drug)]] 0.05 µM 0.0550× (z -11.3) |
| [[LoVo (line)]] | wt | 1.38 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +9.9) | — |
| [[SW480 (line)]] | alt | 1.59 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.04× (z +10.0) | — |
| [[A498 (line)]] | wt | 1.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 46.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 1.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 2.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.62× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 1.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.190× (z -9.4) ⚠ cell-cycle shift, explains ~14% of this change |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1677), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OBI1-AS1]] | +0.85 | +0.82 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SORCS1]] | +0.80 | +0.77 / +0.81 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.79 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.76 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[KCNAB1]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[HPSE2]] | +0.76 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.75 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.75 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[KCNIP1]] | +0.75 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[HULC]] | +0.74 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[CLDN14]] | +0.73 | +0.59 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02240]] | B | LINC02240 activity raises ESR1's level | lines that do not express LINC02240 (35) vs lines expressing it (15) | 1.88× lower at baseline in the lines without LINC02240 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02941, CHL1, EDNRB; maybe low, not absent |
| [[PSG4]] | B | PSG4 activity raises ESR1's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 2.25× lower at baseline in the lines without PSG4 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5 |
| [[FYB1]] | B | FYB1 activity raises ESR1's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without FYB1 | 0.027 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[LINC00536]] | B | LINC00536 activity raises ESR1's level | lines that do not express LINC00536 (17) vs lines expressing it (33) | 1.89× lower at baseline in the lines without LINC00536 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, DOCK2, LDOC1; maybe low, not absent |
| [[LINC02220]] | B | LINC02220 activity raises ESR1's level | lines that do not express LINC02220 (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without LINC02220 | 0.039 | ⚠ within organs, on part of the lines; also absent: COL16A1, SEMA5A, ANKRD30B; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ESR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CTTNBP2]] | B | CTTNBP2 activity raises ESR1's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 1.39× lower at baseline in the lines without CTTNBP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR |
| [[PGR]] | B | PGR activity raises ESR1's level | lines that do not express PGR (36) vs lines expressing it (14) | 1.52× lower at baseline in the lines without PGR | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent |
| [[LINC01098]] | B | LINC01098 activity raises ESR1's level | lines that do not express LINC01098 (36) vs lines expressing it (14) | 1.64× lower at baseline in the lines without LINC01098 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC02109, GREM1, ENSG00000288098; maybe low, not absent |
| [[LINC00383]] | B | LINC00383 activity raises ESR1's level | lines that do not express LINC00383 (39) vs lines expressing it (11) | 1.80× lower at baseline in the lines without LINC00383 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000259639, LINC01425, ENSG00000285751 |
| [[LINC02335]] | B | LINC02335 activity raises ESR1's level | lines that do not express LINC02335 (41) vs lines expressing it (9) | 2.16× lower at baseline in the lines without LINC02335 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02476, ENSG00000285751, ENSG00000234426 |
| [[DIRC3]] | B | DIRC3 activity raises ESR1's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.83× lower at baseline in the lines without DIRC3 | 0.097 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.879). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.8, 27.8); signed map (31.7, 14.7). **Vector** length 62.0, 9.27% of its response variance represented; |z| ≥ 3 in 1,092 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +25.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +21.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +12.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +2.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -2.2 | +1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +1.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | estrogen receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1-q25.2 — chr6:151,656,691-152,129,619 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ER, NR3A1, Era, ER-alpha; previously ESR |
| Gene groups (HGNC) | Estrogen receptors |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 30 pathways, smallest: RUNX1 regulates transcription of genes involved in WNT signaling; RUNX1 regulates estrogen receptor mediated transcription; TFAP2 (AP-2) family regulates transcription of growth factors and their receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P03372](https://www.uniprot.org/uniprotkb/P03372) (Estrogen receptor):

> Nuclear hormone receptor. The steroid hormones and their receptors are involved in the regulation of eukaryotic gene expression and affect cellular proliferation and differentiation in target tissues. Ligand-dependent nuclear transactivation involves either direct homodimer binding to a palindromic estrogen response element (ERE) sequence or association with other DNA-binding transcription factors, such as AP-1/c-Jun, c-Fos, ATF-2, Sp1 and Sp3, to mediate ERE-independent signaling. Ligand …

**Summary**, from NCBI Gene [2099](https://www.ncbi.nlm.nih.gov/gene/2099):

> This gene encodes an estrogen receptor and ligand-activated transcription factor. The canonical protein contains an N-terminal ligand-independent transactivation domain, a central DNA binding domain, a hinge domain, and a C-terminal ligand-dependent transactivation domain. The protein localizes to the nucleus where it may form either a homodimer or a heterodimer with estrogen receptor 2. The protein encoded by this gene regulates the transcription of many estrogen-inducible genes that play a …

**Accessions** — [HGNC:3467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3467) · Entrez [2099](https://www.ncbi.nlm.nih.gov/gene/2099) · UniProt [P03372](https://www.uniprot.org/uniprotkb/P03372) · Ensembl [ENSG00000091831](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091831)

## Data

Gene col 1677: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1677); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1677, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1677]; `tensor/DDL_lfc|DDL_z.npy` [1677]; `embed/gene_vectors.npy` [1677]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1677 or target_col == 1677). Every well: [[ESR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
