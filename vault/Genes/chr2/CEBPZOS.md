---
symbol: "CEBPZOS"
type: "gene"
col: 13292
ensembl_id: "ENSG00000218739"
name: "CEBPZ opposite strand"
location: "2p22.2"
module: 52
arm: "-"
pooled_cpm: 39.96
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# CEBPZOS

*CEBPZ opposite strand* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.55× (z +15.1, q 0e+00, up in 43 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.28× (z +5.7, q 1e-06, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.706× (z -7.9, q 2e-12, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYPLAL1]] (+0.57, fdr 1e-05), [[RBM41]] (+0.56, fdr 2e-05), [[C2orf68]] (+0.53, fdr 3e-05); moves opposite to [[SLC10A3]] (-0.54, fdr 2e-05), [[TOP3A]] (-0.53, fdr 2e-05), [[NPIPB14P]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13292.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +15.1 | 0e+00 | 43/45 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +13.3 | 4e-38 | 37/40 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +8.5 | 3e-15 | 36/44 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +7.0 | 4e-10 | 36/47 (NCI-H2030, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +5.7 | 1e-06 | 32/46 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +5.7 | 1e-06 | 26/48 (A498, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +4.6 | 3e-04 | 24/48 (HT-29, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.0 | 0.004 | 23/47 (LoVo, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.017 | 19/48 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.021 | 22/48 (A-427, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.24×** | +3.5 | 0.024 | 18/48 (KATO III, A498, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.029 | 17/48 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **1.21×** | +3.1 | 0.087 | 14/47 (LoVo, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13292.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.706×** | -7.9 | 2e-12 | 36/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.704×** | -5.6 | 5e-06 | 31/48 (C-33 A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.578×** | -4.6 | 8e-04 | 24/48 (NCI-H460, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.600×** | -4.3 | 0.003 | 26/48 (SW480, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.834× | -4.1 | 0.004 | 22/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.775×** | -4.1 | 0.004 | 24/48 (SNU-423, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.035 | 19/47 (J82, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.809×** | -3.4 | 0.048 | 19/47 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13292. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 32.7 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 2.29× (z +11.3) | — |
| [[A-427 (line)]] | wt | 55.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -15.3) |
| [[NCI-H460 (line)]] | wt | 58.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -15.3) |
| [[A-172 (line)]] | wt | 39.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 44.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +11.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 60.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +11.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 33.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 27.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -9.5) |
| [[PANC-1 (line)]] | alt | 49.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +9.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 53.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 31.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.8) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 38.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.109× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 27.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +9.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 34.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 47.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +10.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 36.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 41.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +10.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 50.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 31.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.17× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 36.0 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0832× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 43.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -10.0) |
| [[SW480 (line)]] | alt | 51.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +9.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13292), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPLAL1]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[RBM41]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[C2orf68]] | +0.53 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[RAD23B]] | +0.52 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[MRPL19]] | +0.52 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[SYNJ2BP]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[TAB2]] | +0.50 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ZSCAN30]] | +0.48 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[PIGM]] | +0.48 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[SCRN3]] | +0.48 | +0.36 / +0.46 | both halves | 9e-05 |  |
| [[METTL5]] | +0.48 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[ZNF780A]] | +0.48 | +0.33 / +0.59 | both halves | 1e-04 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC10A3]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[TOP3A]] | -0.53 | -0.49 / -0.58 | both halves | 2e-05 |  |
| [[NPIPB14P]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[NDEL1]] | -0.52 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[IVNS1ABP]] | -0.51 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[POLG]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[CENPJ]] | -0.48 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ZMYND19]] | -0.48 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[SYVN1]] | -0.48 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[HAUS8]] | -0.48 | -0.23 / -0.59 | both halves | 5e-04 |  |
| [[IKZF4]] | -0.47 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[MYO19]] | -0.47 | -0.38 / -0.55 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.366). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-27.6, -14.1); signed map (-19.5, -20.9). **Vector** length 74.6, 15.9% of its response variance represented; |z| ≥ 3 in 696 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.0 | +3.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -7.2 | -4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.8 | +0.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.4 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | CEBPZ opposite strand |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:37,196,488-37,216,193 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CEBPZ-AS1 |
| Matched by | ensembl_id |

UniProt [A8MTT3](https://www.uniprot.org/uniprotkb/A8MTT3) carries no function annotation.

**Summary**, from NCBI Gene [100505876](https://www.ncbi.nlm.nih.gov/gene/100505876):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:49288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49288) · Entrez [100505876](https://www.ncbi.nlm.nih.gov/gene/100505876) · UniProt [A8MTT3](https://www.uniprot.org/uniprotkb/A8MTT3) · Ensembl [ENSG00000218739](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000218739)

## Data

Gene col 13292: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13292); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13292, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13292]; `tensor/DDL_lfc|DDL_z.npy` [13292]; `embed/gene_vectors.npy` [13292]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13292 or target_col == 13292). Every well: [[CEBPZOS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEBPZOS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
