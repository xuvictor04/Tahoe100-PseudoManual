---
symbol: "TGDS"
type: "gene"
col: 1535
ensembl_id: "ENSG00000088451"
name: "TDP-glucose 4,6-dehydratase"
location: "13q32.1"
module: 41
arm: "+"
pooled_cpm: 27.64
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# TGDS

*TDP-glucose 4,6-dehydratase* — 13q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.77× (z +8.4, q 3e-14, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.541× (z -9.0, q 1e-16, down in 34 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.702× (z -5.2, q 2e-05, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UFL1]] (+0.73, fdr 7e-06), [[RINT1]] (+0.68, fdr 7e-06), [[CDK7]] (+0.68, fdr 7e-06); moves opposite to [[MAPRE1]] (-0.59, fdr 7e-06), [[KPNA4]] (-0.59, fdr 2e-05), [[PITPNB]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +8.4 | 3e-14 | 33/46 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +6.2 | 1e-07 | 28/47 (HT-29, SW480, …) | two highest doses | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +4.7 | 5e-04 | 17/48 (LOX-IMVI, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.098 | 15/48 (Panc 03.27, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1535.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.541×** | -9.0 | 1e-16 | 34/41 (A498, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.537×** | -8.4 | 1e-14 | 23/37 (J82, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -7.5 | 1e-11 | 27/35 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -5.5 | 5e-06 | 5/48 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.702×** | -5.2 | 2e-05 | 24/48 (HOP62, H4, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.739×** | -4.4 | 8e-04 | 21/48 (C32, SW 900, …) | top dose only | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.753×** | -4.2 | 0.002 | 17/48 (J82, HOP62, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.746×** | -4.1 | 0.002 | 18/48 (NCI-H2030, RKO, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **0.819×** | -3.9 | 0.006 | 19/48 (NCI-H661, A-172, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.824×** | -3.9 | 0.006 | 20/48 (Hs 766T, A498, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -3.7 | 0.012 | 13/48 (LoVo, SW480, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **0.781×** | -3.6 | 0.014 | 18/46 (RPMI-7951, SNU-1, …) | rises with dose | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **0.831×** | -3.6 | 0.015 | 18/48 (A-427, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.785×** | -3.6 | 0.015 | 18/48 (COLO 205, J82, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.790×** | -3.5 | 0.020 | 14/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.796×** | -3.3 | 0.029 | 12/48 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.801×** | -3.3 | 0.037 | 13/48 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.810×** | -3.1 | 0.059 | 12/48 (SW 1088, A498, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.814×** | -3.0 | 0.072 | 8/48 (SW 1088, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 48.1 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.8) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.21× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0422× (z -33.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 88.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -15.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 61.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 28.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -11.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 23.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -14.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 26.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -11.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0718× (z -8.7) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -9.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -8.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -11.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -10.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -11.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFL1]] | +0.73 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[RINT1]] | +0.68 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[CDK7]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[UBA5]] | +0.66 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[ESCO1]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CRLS1]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[NFXL1]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ALG5]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 | STRING 487 |
| [[KLHL28]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[CCS]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[DUSP11]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[DNAJC25]] | +0.63 | +0.67 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.59 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[KPNA4]] | -0.59 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[PITPNB]] | -0.57 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[RASAL2]] | -0.55 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.55 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[ZNF407]] | -0.55 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[PSMD1]] | -0.55 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[RAB10]] | -0.55 | -0.46 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (6.9, -33.4); signed map (-14.6, 2.2). **Vector** length 100, 23.7% of its response variance represented; |z| ≥ 3 in 772 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.4 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +8.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.2 | +3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.8 | +2.9 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | -9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.8 | -8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -4.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.6 | -4.2 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | TDP-glucose 4,6-dehydratase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.1 — chr13:94,574,054-94,596,242 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TDPGD, SDR2E1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily; Carbon-oxygen lyases |
| Matched by | ensembl_id |

**Function**, from UniProt [O95455](https://www.uniprot.org/uniprotkb/O95455) (UDP-D-glucose 4,6-dehydratase):

> UDP-glucose 4,6-dehydratase that converts UDP-glucose into UDP-4-keto-6-deoxyglucose, and which is required for glycosaminoglycan biosynthesis and skeletal development. UDP-4-keto-6-deoxyglucose is a mimic of the reaction intermediate of UXS1 and acts as an enzyme-rescue metabolite to promote the completion of UXS1 catalytic cycle when NAD(+) levels are low. Under low NAD(+) conditions, UXS1 forms an inactive UDP-4-ketoxylose intermediate bound to NADH, impairing the synthesis of specific …

**Summary**, from NCBI Gene [23483](https://www.ncbi.nlm.nih.gov/gene/23483):

> The protein encoded by this gene is a member of the short-chain dehydrogenases/reductases (SDR) superfamily, and is thought to contain a nicotinamide adenine dinucleotide (NAD) binding domain. This large SDR family of enzymes is involved in the metabolism of a variety of compounds, including prostaglandins, retinoids, lipids, steroid hormones, and xenobiotics. Mutations in this gene have been associated with Catel-Manzke syndrome, which is characterized by Pierre Robin sequence, and radial …

**Accessions** — [HGNC:20324](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20324) · Entrez [23483](https://www.ncbi.nlm.nih.gov/gene/23483) · UniProt [O95455](https://www.uniprot.org/uniprotkb/O95455) · Ensembl [ENSG00000088451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088451)

## Data

Gene col 1535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1535); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1535]; `tensor/DDL_lfc|DDL_z.npy` [1535]; `embed/gene_vectors.npy` [1535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1535 or target_col == 1535). Every well: [[TGDS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGDS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
