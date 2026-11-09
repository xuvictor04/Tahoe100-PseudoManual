---
symbol: "IQUB"
type: "gene"
col: 8986
ensembl_id: "ENSG00000164675"
name: "IQ motif and ubiquitin domain containing"
location: "7q31.32"
module: 37
arm: "+"
pooled_cpm: 3.66
n_lines_expressing: 48
n_dd_up: 37
n_dd_down: 2
n_dd_up_clean: 29
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# IQUB

*IQ motif and ubiquitin domain containing* — 7q31.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.25× (z +23.8, q 0e+00, up in 32 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Gallic acid (hydrate) (drug)]] 0.05 µM: 0.685× (z -3.8, q 0.050, down in 7 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW480 0.0719×); [[Acetohexamide (drug)]] 0.5 µM in 1 line (SHP-77 0.112×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02763]] (+0.63, fdr 7e-06), [[MGC4859]] (+0.60, fdr 1e-05), [[KLC4]] (+0.60, fdr 2e-05); moves opposite to [[MACROH2A1]] (-0.58, fdr 3e-05), [[HNRNPAB]] (-0.57, fdr 2e-05), [[SRPK1]] (-0.57, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8986.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.25×** | +23.8 | 0e+00 | 32/35 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **8.00×** | +21.1 | 0e+00 | 42/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **5.82×** | +17.8 | 0e+00 | 41/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.33×** | +17.2 | 0e+00 | 30/34 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.70×** | +15.7 | 0e+00 | 40/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.84×** | +13.6 | 2e-40 | 27/35 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.21×** | +11.4 | 6e-28 | 15/21 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **6.54×** | +10.0 | 2e-21 | 32/38 (NCI-H460, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.63×** | +9.8 | 8e-21 | 32/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.63×** | +9.8 | 8e-21 | 31/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **4.19×** | +7.6 | 2e-12 | 20/35 (LoVo, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +7.1 | 7e-11 | 20/39 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +6.5 | 3e-09 | 16/41 (SW 900, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.94×** | +6.5 | 4e-09 | 1/6 (HOP62) | inconsistent across doses | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +6.3 | 1e-08 | 13/29 (HS-578T, SW 900, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.8 | 2e-07 | 16/45 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.77×** | +5.7 | 3e-07 | 18/34 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8986.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 0.05 µM in 1 line (SW480 0.0719×); [[Acetohexamide (drug)]] 0.5 µM in 1 line (SHP-77 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.685×** | -3.8 | 0.050 | 7/43 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.692×** | -3.8 | 0.050 | 10/44 (C-33 A, AN3 CA, …) | top dose only | position effect removed |
| [[Allantoin (drug)]] 5 µM |  | 0.788× | -3.5 | 0.10 | 13/44 (HCT15, HOP62, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.720× | -3.4 | 0.11 | 3/43 (SW 900, C32, …) | inconsistent across doses |  |
| [[Baicalin (drug)]] 0.5 µM |  | 0.729× | -3.2 | 0.14 | 10/43 (NCI-H1792, H4, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.744× | -3.0 | 0.24 | 10/44 (NCI-H2030, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.41 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.63× (z +12.2) | — |
| [[NCI-H460 (line)]] | wt | 4.26 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.93× (z +13.9) | — |
| [[SW480 (line)]] | alt | 3.23 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +11.7) | [[Canagliflozin (drug)]] 0.05 µM 0.0719× (z -10.5) |
| [[PANC-1 (line)]] | alt | 2.10 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 17.4× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 3.75 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +10.5) | — |
| [[LoVo (line)]] | wt | 3.32 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +12.4) | — |
| [[C32 (line)]] | wt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.34× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 6.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.16× (z +9.6) | — |
| [[KATO III (line)]] | alt | 3.64 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 15.1× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 4.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.71× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 3.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.21× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 9.58 | 0 | 1 | — | [[Acetohexamide (drug)]] 0.5 µM 0.112× (z -9.0) |
| [[A-172 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.865 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.903 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02763]] | +0.63 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[MGC4859]] | +0.60 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[KLC4]] | +0.60 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[MYLK3]] | +0.60 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[CD247]] | +0.59 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[ADCY10]] | +0.59 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[LINC00640]] | +0.58 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[NME9]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ECT2L]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ELOA-AS1]] | +0.57 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[DNAI7]] | +0.56 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[SLC23A1]] | +0.56 | +0.62 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACROH2A1]] | -0.58 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[HNRNPAB]] | -0.57 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[SRPK1]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[LETM1]] | -0.56 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CTPS1]] | -0.56 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[MTAP]] | -0.55 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[LRP8]] | -0.53 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[WDR4]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[HERC2]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ZBED4]] | -0.51 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CCT6A]] | -0.51 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[SPECC1L]] | -0.51 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IQUB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.488). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.2, 17.9); signed map (9.8, 3.6). **Vector** length 49.1, 6.12% of its response variance represented; |z| ≥ 3 in 1,203 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +3.9 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +23.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.5 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +7.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.4 | +5.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.4 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.0 | -3.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.0 | -2.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.0 | -0.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -0.9 | -0.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif and ubiquitin domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.32 — chr7:123,452,193-123,535,077 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35834 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NA54](https://www.uniprot.org/uniprotkb/Q8NA54) (IQ motif and ubiquitin-like domain-containing protein):

> Adapter protein that anchors the radial spoke 1 (RS1) complex to the A microtubule of outer doublet microtubules in axonemes. The triple radial spokes (RS1, RS2 and RS3) are required to modulate beating of the sperm flagellum. May play a role in inhibiting signaling via MAPK1/ERK2 and MAPK3/ERK1. Additionally, may play a role in the functioning of cilia (By similarity). Not required for the functioning of tracheal or ependymal cilia (By similarity).

**Summary**, from NCBI Gene [154865](https://www.ncbi.nlm.nih.gov/gene/154865):

> Involved in flagellated sperm motility and mating. Predicted to be located in sperm flagellum. Predicted to be part of radial spoke. Predicted to be active in acrosomal vesicle and motile cilium. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21995) · Entrez [154865](https://www.ncbi.nlm.nih.gov/gene/154865) · UniProt [Q8NA54](https://www.uniprot.org/uniprotkb/Q8NA54) · Ensembl [ENSG00000164675](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164675)

## Data

Gene col 8986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8986); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8986]; `tensor/DDL_lfc|DDL_z.npy` [8986]; `embed/gene_vectors.npy` [8986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8986 or target_col == 8986). Every well: [[IQUB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQUB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
