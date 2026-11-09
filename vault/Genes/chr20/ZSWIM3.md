---
symbol: "ZSWIM3"
type: "gene"
col: 5374
ensembl_id: "ENSG00000132801"
name: "zinc finger SWIM-type containing 3"
location: "20q13.12"
module: 170
arm: "+"
pooled_cpm: 7.37
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# ZSWIM3

*zinc finger SWIM-type containing 3* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.95× (z +20.3, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.501× (z -7.3, q 2e-10, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF490]] (+0.75, fdr 7e-06), [[FBXO28]] (+0.70, fdr 9e-06), [[NDUFAF1]] (+0.68, fdr 7e-06); moves opposite to [[PRKDC]] (-0.64, fdr 1e-05), [[NONO]] (-0.61, fdr 7e-06), [[SPIDR]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5374.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.95×** | +20.3 | 0e+00 | 40/40 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.67×** | +10.3 | 2e-22 | 39/47 (PANC-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +8.5 | 3e-15 | 24/37 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +8.5 | 3e-15 | 32/48 (Panc 03.27, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.19×** | +8.2 | 3e-14 | 31/47 (A-427, PANC-1, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +7.8 | 7e-13 | 25/39 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +7.5 | 6e-12 | 26/48 (SW1417, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +5.5 | 3e-06 | 17/32 (SW1417, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +5.1 | 2e-05 | 22/47 (A-427, PANC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +4.9 | 5e-05 | 20/44 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +4.4 | 5e-04 | 12/38 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +4.4 | 5e-04 | 17/44 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +4.2 | 9e-04 | 11/42 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.002 | 19/41 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.013 | 16/43 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.013 | 13/46 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5374.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.501×** | -7.3 | 2e-10 | 25/45 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.541×** | -6.5 | 3e-08 | 25/47 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.557×** | -6.2 | 1e-07 | 24/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.580×** | -5.7 | 1e-06 | 21/38 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -5.6 | 2e-06 | 25/35 (NCI-H2347, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.656×** | -4.3 | 0.002 | 13/40 (LS 180, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 14.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.207× (z -9.1) ⚠ toxic |
| [[SW1417 (line)]] | alt | 17.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -8.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 5.43 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +12.4) | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0913× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0734× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Oxaprozin (drug)]] 0.5 µM 0.0948× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 4.94 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.61× (z +10.7) | [[Ixazomib citrate (drug)]] 5 µM 0.0813× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 10.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.95× (z +11.5) | [[Docetaxel (drug)]] 0.05 µM 0.148× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~61% of this change |
| [[PANC-1 (line)]] | alt | 6.97 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.16× (z +15.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -10.7) |
| [[SW480 (line)]] | alt | 13.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +14.6) | — |
| [[A-172 (line)]] | wt | 5.43 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0678× (z -10.3) ⚠ cell-cycle shift, explains ~11% of this change |
| [[BT-474 (line)]] | alt | 5.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.87× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0537× (z -12.4) ⚠ toxic |
| [[HT-29 (line)]] | alt | 6.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.38× (z +10.7) | — |
| [[KATO III (line)]] | alt | 5.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.50× (z +10.0) | — |
| [[LoVo (line)]] | wt | 5.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.43× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 4.53 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0755× (z -8.9) ⚠ cell-cycle shift, explains ~11% of this change |
| [[NCI-H2347 (line)]] | alt | 5.20 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0840× (z -9.6) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 4.42 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -8.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 6.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.61× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 8.69 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0746× (z -9.9) |
| [[A-427 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF490]] | +0.75 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[FBXO28]] | +0.70 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[NDUFAF1]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ZNF547]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[YJU2B]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ZNF425]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ZNF791]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[S100A13]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[PIN4]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[TJAP1]] | +0.63 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[HSCB]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.64 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[NONO]] | -0.61 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[SPIDR]] | -0.61 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.60 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[TRAF7]] | -0.59 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[LBR]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TBCD]] | -0.59 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[ICMT]] | -0.57 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[PARP1]] | -0.57 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[NIN]] | -0.57 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[TUBB]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[CS]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZSWIM3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.5% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-39.6, 4.2); signed map (-4.1, -11.3). **Vector** length 74.0, 12.9% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +20.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +7.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.7 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | +1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -7.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger SWIM-type containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,857,614-45,879,122 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ337O18.7, PPP1R174; previously C20orf164 |
| Gene groups (HGNC) | Zinc fingers SWIM-type |
| Matched by | ensembl_id |

UniProt [Q96MP5](https://www.uniprot.org/uniprotkb/Q96MP5) carries no function annotation.

**Summary**, from NCBI Gene [140831](https://www.ncbi.nlm.nih.gov/gene/140831):

> Predicted to enable zinc ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16157) · Entrez [140831](https://www.ncbi.nlm.nih.gov/gene/140831) · UniProt [Q96MP5](https://www.uniprot.org/uniprotkb/Q96MP5) · Ensembl [ENSG00000132801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132801)

## Data

Gene col 5374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5374); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5374]; `tensor/DDL_lfc|DDL_z.npy` [5374]; `embed/gene_vectors.npy` [5374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5374 or target_col == 5374). Every well: [[ZSWIM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSWIM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
