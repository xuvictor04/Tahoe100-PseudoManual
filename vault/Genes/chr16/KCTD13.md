---
symbol: "KCTD13"
type: "gene"
col: 10546
ensembl_id: "ENSG00000174943"
name: "potassium channel tetramerization domain containing 13"
location: "16p11.2"
module: 2
arm: "+"
pooled_cpm: 24.14
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# KCTD13

*potassium channel tetramerization domain containing 13* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.19× (z +13.6, q 3e-39, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.200×, A-172 0.344×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 0.181×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.148×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKMY1]] (+0.61, fdr 1e-05), [[MEF2B]] (+0.58, fdr 1e-05), [[CAMSAP1-DT]] (+0.57, fdr 1e-05); moves opposite to [[FAM13A]] (-0.55, fdr 1e-05), [[TIPARP]] (-0.54, fdr 1e-04), [[PHF21A]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10546.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.19×** | +13.6 | 3e-39 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +12.7 | 3e-34 | 44/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +10.2 | 5e-22 | 37/45 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +10.1 | 9e-22 | 45/48 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +9.9 | 7e-21 | 35/47 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +7.8 | 7e-13 | 33/47 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.9 | 7e-05 | 22/48 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.7 | 2e-04 | 21/48 (A498, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.27×** | +4.2 | 0.002 | 15/47 (C32, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.002 | 15/48 (AsPC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.002 | 18/47 (MIA PaCa-2, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.022 | 17/47 (MIA PaCa-2, AN3 CA, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.22×** | +3.4 | 0.031 | 8/47 (A498, LoVo, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.031 | 15/48 (LoVo, J82, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +3.2 | 0.053 | 10/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10546.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.200×, A-172 0.344×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 0.181×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.148×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.896× | -6.4 | 9e-08 | 4/48 (HOP62, Hs 766T, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.822× | -3.3 | 0.30 | 9/48 (A549, CFPAC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.709× | -3.1 | 0.36 | 14/45 (A498, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 25.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.6) | — |
| [[SW480 (line)]] | alt | 29.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.41× (z +9.0) | — |
| [[A-172 (line)]] | wt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[A-427 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[A549 (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 27.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.42× (z +9.0) ⚠ toxic | — |
| [[HOP62 (line)]] | alt | 17.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 23.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.148× (z -9.3) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKMY1]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[MEF2B]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[CAMSAP1-DT]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[NPLOC4]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TTL]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[KLC1]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[CCM2]] | +0.55 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[LTO1]] | +0.55 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[UBE2F-SCLY]] | +0.55 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[MICALL1]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[NUP50-DT]] | +0.54 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[UBE2F]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM13A]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[TIPARP]] | -0.54 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[PHF21A]] | -0.53 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[DMXL2]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[RNF150]] | -0.52 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[DIXDC1]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[HAUS4]] | -0.52 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[ARL4D]] | -0.51 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[BDH2]] | -0.50 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[PPP1R3C]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ZNF608]] | -0.50 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[MDH1]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCTD13's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.360). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (16.8, 1.3); signed map (2.7, 8.6). **Vector** length 72.2, 12.5% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +10.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +3.5 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -0.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | +2.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,905,012-29,926,236 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PDIP1, FKSG86, POLDIP1 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Reactome | 5 pathways, smallest: RND2 GTPase cycle; RND3 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WZ19](https://www.uniprot.org/uniprotkb/Q8WZ19) (BTB/POZ domain-containing adapter for CUL3-mediated RhoA degradation protein 1):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex required for synaptic transmission. The BCR(KCTD13) E3 ubiquitin ligase complex mediates the ubiquitination of RHOA, leading to its degradation by the proteasome Degradation of RHOA regulates the actin cytoskeleton and promotes synaptic transmission (By similarity). Mediates also the ubiquitination and degradation of GluN1/GRIN1 to regulate excitatory synaptic transmission and seizure susceptibility.

**Summary**, from NCBI Gene [253980](https://www.ncbi.nlm.nih.gov/gene/253980):

> Enables identical protein binding activity and ubiquitin-like ligase-substrate adaptor activity. Involved in several processes, including negative regulation of Rho protein signal transduction; proteasome-mediated ubiquitin-dependent protein catabolic process; and stress fiber assembly. Located in nuclear body. Part of Cul3-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22234) · Entrez [253980](https://www.ncbi.nlm.nih.gov/gene/253980) · UniProt [Q8WZ19](https://www.uniprot.org/uniprotkb/Q8WZ19) · Ensembl [ENSG00000174943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174943)

## Data

Gene col 10546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10546); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10546]; `tensor/DDL_lfc|DDL_z.npy` [10546]; `embed/gene_vectors.npy` [10546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10546 or target_col == 10546). Every well: [[KCTD13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
