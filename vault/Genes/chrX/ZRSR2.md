---
symbol: "ZRSR2"
type: "gene"
col: 9785
ensembl_id: "ENSG00000169249"
name: "zinc finger CCCH-type, RNA binding motif and serine/arginine rich 2"
location: "Xp22.2"
module: 41
arm: "+"
pooled_cpm: 40.96
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ZRSR2

*zinc finger CCCH-type, RNA binding motif and serine/arginine rich 2* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.08× (z +10.7, q 4e-24, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.700× (z -5.0, q 3e-04, down in 22 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.748× (z -4.3, q 0.006, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UFL1]] (+0.77, fdr 7e-06), [[SAFB2]] (+0.74, fdr 7e-06), [[NKAP]] (+0.72, fdr 7e-06); moves opposite to [[VMA21]] (-0.69, fdr 7e-06), [[GNG12]] (-0.62, fdr 7e-06), [[ACTB]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9785.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +10.7 | 4e-24 | 41/47 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +7.5 | 2e-11 | 42/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +6.2 | 9e-08 | 30/47 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 4e-05 | 32/48 (LS 180, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +5.1 | 5e-05 | 30/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.004 | 23/48 (C-33 A, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +4.1 | 0.004 | 26/48 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.097 | 15/48 (RKO, HepG2/C3A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9785.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.700×** | -5.0 | 3e-04 | 22/38 (HCT15, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.748×** | -4.3 | 0.006 | 24/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.741×** | -4.1 | 0.009 | 22/40 (Hs 766T, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | **0.776×** | -3.7 | 0.027 | 21/48 (NCI-H1573, SW1417, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.780×** | -3.6 | 0.027 | 20/48 (A549, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.781×** | -3.6 | 0.027 | 22/48 (A498, HS-578T, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.783×** | -3.6 | 0.027 | 21/48 (A498, LS 180, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.785×** | -3.6 | 0.027 | 20/48 (SW 1088, A549, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.793×** | -3.4 | 0.043 | 19/48 (Panc 03.27, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -3.2 | 0.081 | 18/48 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.806×** | -3.2 | 0.081 | 15/48 (A549, KATO III, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.809×** | -3.1 | 0.087 | 15/48 (LS 180, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.810×** | -3.1 | 0.087 | 18/48 (A498, NCI-H2347, …) | all doses, flat |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.812×** | -3.0 | 0.093 | 13/48 (NCI-H2030, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 73.1 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.404× (z -10.1) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.436× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 52.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.351× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 45.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -11.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 47.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.7) | — |
| [[LoVo (line)]] | wt | 25.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 26.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.15× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 35.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.81× (z +10.6) | — |
| [[SW480 (line)]] | alt | 52.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +12.1) | — |
| [[A-427 (line)]] | wt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.80× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.272× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 29.8 | 0 | 1 | — | [[BI-3406 (drug)]] 0.05 µM 0.0547× (z -10.6) |
| [[HCT15 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -11.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 57.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 85.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[RKO (line)]] | wt | 43.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.14× (z +9.1) | — |
| [[A-172 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFL1]] | +0.77 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[SAFB2]] | +0.74 | +0.78 / +0.64 | both halves | 7e-06 | same gene group |
| [[NKAP]] | +0.72 | +0.71 / +0.68 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TMF1]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.72 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[CCDC186]] | +0.69 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[PPIL4]] | +0.69 | +0.71 / +0.59 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ERCC5]] | +0.68 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[MED10]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[AKAP9]] | +0.66 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[ZFPL1]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[KLC4]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.69 | -0.69 / -0.63 | both halves | 7e-06 |  |
| [[GNG12]] | -0.62 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[ACTB]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[C1QBP]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[TMEM19]] | -0.56 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[RBBP7]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[TGOLN2]] | -0.56 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[CHML]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers ZRSR2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.736). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.0, -38.4); signed map (-50.2, 15.7). **Vector** length 111, 31.0% of its response variance represented; |z| ≥ 3 in 751 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +10.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.0 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.3 | +7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +5.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +4.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +0.7 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.8 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.7 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.9 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -2.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.1 | -3.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.1 | -3.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCCH-type, RNA binding motif and serine/arginine rich 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:15,790,156-15,830,694 (+) |
| Ensembl biotype | protein_coding |
| Also known as | U2AF1-RS2, URP, ZC3H22; previously U2AF1L2 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; RNA binding motif containing; U11/U12 di-snRNP |
| Reactome | 4 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15696](https://www.uniprot.org/uniprotkb/Q15696) (U2 small nuclear ribonucleoprotein auxiliary factor 35 kDa subunit-related protein 2):

> Pre-mRNA-binding protein required for splicing of both U2- and U12-type introns. Selectively interacts with the 3'-splice site of U2- and U12-type pre-mRNAs and promotes different steps in U2 and U12 intron splicing. Recruited to U12 pre-mRNAs in an ATP-dependent manner and is required for assembly of the pre-spliceosome, a precursor to other spliceosomal complexes. For U2-type introns, it is selectively and specifically required for the second step of splicing.

**Summary**, from NCBI Gene [8233](https://www.ncbi.nlm.nih.gov/gene/8233):

> This gene encodes an essential splicing factor. The encoded protein associates with the U2 auxiliary factor heterodimer, which is required for the recognition of a functional 3' splice site in pre-mRNA splicing, and may play a role in network interactions during spliceosome assembly. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23019](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23019) · Entrez [8233](https://www.ncbi.nlm.nih.gov/gene/8233) · UniProt [Q15696](https://www.uniprot.org/uniprotkb/Q15696) · Ensembl [ENSG00000169249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169249)

## Data

Gene col 9785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9785); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9785]; `tensor/DDL_lfc|DDL_z.npy` [9785]; `embed/gene_vectors.npy` [9785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9785 or target_col == 9785). Every well: [[ZRSR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZRSR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
