---
symbol: "PWP1"
type: "gene"
col: 5804
ensembl_id: "ENSG00000136045"
name: "PWP1 homolog, endonuclein"
location: "12q23.3"
module: 1
arm: "+"
pooled_cpm: 49.53
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 5
n_dd_up_clean: 21
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PWP1

*PWP1 homolog, endonuclein* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.49× (z +8.7, q 1e-15, up in 31 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.48× (z +8.7, q 1e-15, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.631× (z -14.5, q 1e-44, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM28]] (+0.69, fdr 7e-06), [[DDX1]] (+0.69, fdr 7e-06), [[PTCD2]] (+0.68, fdr 7e-06); moves opposite to [[PPP1R15B-AS1]] (-0.52, fdr 8e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5804.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +8.7 | 1e-15 | 31/47 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +8.7 | 1e-15 | 40/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +8.3 | 1e-14 | 36/48 (NCI-H1792, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +7.5 | 8e-12 | 35/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +5.9 | 5e-07 | 26/47 (NCI-H1573, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[EX229 (drug)]] 5 µM |  | **1.64×** | +5.7 | 1e-06 | 32/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +5.6 | 1e-06 | 27/48 (SHP-77, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.6 | 2e-06 | 22/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +5.4 | 5e-06 | 0/48 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +5.3 | 7e-06 | 24/48 (HepG2/C3A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.27×** | +5.2 | 8e-06 | 26/48 (SHP-77, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +5.0 | 3e-05 | 24/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.8 | 6e-05 | 19/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | **1.24×** | +4.6 | 2e-04 | 19/42 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.5 | 3e-04 | 22/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.5 | 3e-04 | 18/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 4e-04 | 17/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 7e-04 | 18/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +4.0 | 0.002 | 15/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.010 | 11/48 (J82, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.18× | +3.5 | 0.013 | 11/47 (NCI-H460, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5804.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -14.5 | 1e-44 | 41/48 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.807×** | -6.8 | 4e-09 | 26/48 (A-172, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.747×** | -6.5 | 2e-08 | 32/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -5.0 | 7e-05 | 23/48 (SNU-423, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.835× | -4.0 | 0.006 | 16/48 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.835× | -3.9 | 0.010 | 14/48 (RKO, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.843× | -3.8 | 0.011 | 15/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.057 | 19/48 (NCI-H460, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.863× | -3.3 | 0.057 | 18/48 (SNU-1, SW 1088, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -3.3 | 0.057 | 15/48 (HOP62, A-172, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.904× | -3.2 | 0.069 | 15/48 (HOP62, A-172, …) | rises with dose |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.908× | -3.1 | 0.10 | 3/48 (RKO, SK-MEL-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 77.0 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -9.6) |
| [[LoVo (line)]] | wt | 51.4 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -13.3) |
| [[SNU-423 (line)]] | alt | 56.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +8.5) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 70.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -18.6) |
| [[NCI-H460 (line)]] | wt | 59.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -10.6) |
| [[RKO (line)]] | wt | 58.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +8.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -10.0) |
| [[A-172 (line)]] | wt | 46.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -10.6) |
| [[A498 (line)]] | wt | 67.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -12.7) |
| [[C32 (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[CFPAC-1 (line)]] | alt | 45.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 49.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 45.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -11.3) |
| [[HOP62 (line)]] | alt | 44.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 44.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -11.0) |
| [[J82 (line)]] | alt | 56.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 63.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 41.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.27× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 49.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.18× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 43.5 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.385× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 55.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 58.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -11.8) |
| [[A-427 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 47.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM28]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 | STRING 880 |
| [[DDX1]] | +0.69 | +0.67 / +0.71 | both halves | 7e-06 | STRING 403 |
| [[PTCD2]] | +0.68 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[BMS1]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 | STRING 875 |
| [[EIF2B4]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[NUDCD3]] | +0.67 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[WDR70]] | +0.66 | +0.56 / +0.61 | both halves | 1e-05 | same gene group |
| [[TAMM41]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[DLAT]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[AGGF1]] | +0.63 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[BLTP1]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ZNHIT6]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R15B-AS1]] | -0.52 | -0.37 / -0.45 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.504). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.2, -4.7); signed map (-18.1, -24.9). **Vector** length 111, 28.9% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.4 | +7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +8.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.9 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +8.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +4.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.6 | -14.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.9 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | PWP1 homolog, endonuclein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:107,685,799-107,713,162 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IEF-SSP-9502 |
| Gene groups (HGNC) | WD repeat domain containing |
| Hallmark sets | MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13610](https://www.uniprot.org/uniprotkb/Q13610) (Periodic tryptophan protein 1 homolog):

> Chromatin-associated factor that regulates transcription. Regulates Pol I-mediated rRNA biogenesis and, probably, Pol III-mediated transcription. Regulates the epigenetic status of rDNA.

**Summary**, from NCBI Gene [11137](https://www.ncbi.nlm.nih.gov/gene/11137):

> The protein encoded by this gene contains several WD-40 repeats and is found mostly in the nucleus. The expression and localization of this protein are cell cycle dependent. Expression of this gene is upregulated in pancreatic adenocarcinoma. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:17015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17015) · Entrez [11137](https://www.ncbi.nlm.nih.gov/gene/11137) · UniProt [Q13610](https://www.uniprot.org/uniprotkb/Q13610) · Ensembl [ENSG00000136045](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136045)

## Data

Gene col 5804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5804); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5804]; `tensor/DDL_lfc|DDL_z.npy` [5804]; `embed/gene_vectors.npy` [5804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5804 or target_col == 5804). Every well: [[PWP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PWP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
