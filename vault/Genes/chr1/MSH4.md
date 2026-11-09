---
symbol: "MSH4"
type: "gene"
col: 647
ensembl_id: "ENSG00000057468"
name: "mutS homolog 4"
location: "1p31.1"
module: 39
arm: "+"
pooled_cpm: 7.61
n_lines_expressing: 49
n_dd_up: 34
n_dd_down: 6
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# MSH4

*mutS homolog 4* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.66× (z +21.4, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.448× (z -4.1, q 0.014, down in 11 of 36 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM: 0.671× (z -4.0, q 0.014, down in 12 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM15-AS1]] (+0.85, fdr 7e-06), [[ANKDD1B]] (+0.85, fdr 7e-06), [[BAAT]] (+0.83, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 647.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.66×** | +21.4 | 0e+00 | 40/40 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **9.24×** | +21.0 | 0e+00 | 26/27 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.56×** | +17.7 | 0e+00 | 33/39 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.97×** | +13.5 | 1e-39 | 33/38 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.63×** | +13.5 | 3e-39 | 36/46 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.95×** | +13.0 | 1e-36 | 30/36 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.44×** | +11.7 | 1e-29 | 35/40 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.24×** | +11.5 | 5e-29 | 39/44 (LoVo, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.23×** | +11.2 | 4e-27 | 30/45 (NCI-H2347, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **2.71×** | +9.8 | 8e-21 | 31/46 (LoVo, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.14×** | +7.0 | 1e-10 | 23/43 (SNU-1, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +6.7 | 1e-09 | 7/15 (HOP62, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.95×** | +6.6 | 2e-09 | 23/46 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +6.3 | 1e-08 | 19/46 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.30×** | +6.1 | 3e-08 | 6/11 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +4.9 | 4e-05 | 17/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.003 | 7/45 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.004 | 11/40 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[EX229 (drug)]] 5 µM |  | **2.04×** | +3.6 | 0.006 | 7/36 (HCT15, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.008 | 13/46 (SW48, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 647.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.448×** | -4.1 | 0.014 | 11/36 (RKO, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.667×** | -4.0 | 0.014 | 16/39 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.671×** | -4.0 | 0.014 | 12/47 (Hs 766T, SNU-1, …) | all doses, flat | position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.680×** | -3.6 | 0.041 | 10/42 (HEC-1-A, C-33 A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -3.4 | 0.088 | 11/47 (NCI-H1792, PANC-1, …) | all doses, flat | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.709×** | -3.3 | 0.096 | 10/45 (SK-MEL-2, HT-29, …) | top dose only | plate-row cell shift |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.725× | -3.2 | 0.11 | 8/45 (LoVo, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.721× | -3.1 | 0.12 | 4/45 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 647. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 36.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +22.0) | — |
| [[CFPAC-1 (line)]] | alt | 4.10 | 2 (1 ⚠) | 2 | [[Topotecan (hydrochloride) (drug)]] 5 µM 29.2× (z +10.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.18× (z +10.2) | [[Raltitrexed (drug)]] 0.5 µM 0.0685× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 7.20 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +10.5) | [[Temsirolimus (drug)]] 0.5 µM 0.0760× (z -9.3) |
| [[LS 180 (line)]] | wt | 20.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +10.9) | — |
| [[SW480 (line)]] | alt | 3.53 | 3 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 10.6× (z +9.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.73× (z +9.1) | — |
| [[A498 (line)]] | wt | 2.88 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.64× (z +9.0) | — |
| [[C32 (line)]] | wt | 8.08 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 25.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.82× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.75 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 2.43 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 19.4× (z +10.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.87× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 3.27 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.44× (z +11.0) | — |
| [[SW1417 (line)]] | alt | 9.00 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 40.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.141× (z -9.0) |
| [[HOP62 (line)]] | alt | 2.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.18× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 2.44 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 26.6× (z +8.7) ⚠ toxic | — |
| [[HS-578T (line)]] | alt | 4.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.45× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 7.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.83× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0608× (z -10.7) ⚠ transcription drop; unreliable plate only |
| [[A-172 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 647), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM15-AS1]] | +0.85 | +0.83 / +0.63 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.85 | +0.84 / +0.68 | both halves | 7e-06 |  |
| [[BAAT]] | +0.83 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.83 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[PLAC8L1]] | +0.82 | +0.87 / +0.57 | both halves | 1e-05 |  |
| [[ZFHX2-AS1]] | +0.80 | +0.80 / +0.54 | both halves | 1e-05 |  |
| [[LINC02936]] | +0.79 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[ARL9]] | +0.79 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.79 | +0.78 / +0.47 | both halves | 2e-05 |  |
| [[LINC02955]] | +0.78 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[CCT6B]] | +0.78 | +0.80 / +0.44 | both halves | 3e-05 |  |
| [[SLC2A9]] | +0.78 | +0.80 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MSH4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.822). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.2, -12.3); signed map (17.1, 3.9). **Vector** length 79.1, 14.6% of its response variance represented; |z| ≥ 3 in 1,401 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.6 | +11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +13.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +21.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +17.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +21.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +13.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +7.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.6 | +3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +0.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | +6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | mutS homolog 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:75,796,882-75,913,242 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MutS homologs |
| Reactome | 4 pathways, smallest: Meiotic recombination; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [O15457](https://www.uniprot.org/uniprotkb/O15457) (MutS protein homolog 4):

> Involved in meiotic recombination. Required for reciprocal recombination and proper segregation of homologous chromosomes at meiosis.

**Summary**, from NCBI Gene [4438](https://www.ncbi.nlm.nih.gov/gene/4438):

> This gene encodes a member of the DNA mismatch repair mutS family. This member is a meiosis-specific protein that is not involved in DNA mismatch correction, but is required for reciprocal recombination and proper segregation of homologous chromosomes at meiosis I. This protein and MSH5 form a heterodimer which binds uniquely to a Holliday Junction and its developmental progenitor, thus provoking ADP-ATP exchange, and stabilizing the interaction between parental chromosomes during meiosis …

**Accessions** — [HGNC:7327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7327) · Entrez [4438](https://www.ncbi.nlm.nih.gov/gene/4438) · UniProt [O15457](https://www.uniprot.org/uniprotkb/O15457) · Ensembl [ENSG00000057468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000057468)

## Data

Gene col 647: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 647); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 647, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 647]; `tensor/DDL_lfc|DDL_z.npy` [647]; `embed/gene_vectors.npy` [647]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 647 or target_col == 647). Every well: [[MSH4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSH4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
