---
symbol: "VPS4B"
type: "gene"
col: 4078
ensembl_id: "ENSG00000119541"
name: "vacuolar protein sorting 4 homolog B"
location: "18q21.33"
module: 41
arm: "+"
pooled_cpm: 77.69
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# VPS4B

*vacuolar protein sorting 4 homolog B* — 18q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.51× (z +13.6, q 2e-39, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.781× (z -11.5, q 9e-28, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V1D]] (+0.62, fdr 1e-05), [[EMC3]] (+0.58, fdr 1e-05), [[TMUB2]] (+0.58, fdr 3e-05); moves opposite to [[ZNF592]] (-0.53, fdr 6e-05), [[ASB13]] (-0.50, fdr 3e-05), [[LRRC8B]] (-0.49, fdr 4e-04).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4078.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +13.6 | 2e-39 | 40/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +13.2 | 2e-37 | 41/49 (LS 180, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +12.9 | 6e-36 | 36/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +10.6 | 4e-24 | 38/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +9.4 | 4e-19 | 35/48 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +8.9 | 6e-17 | 22/49 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +8.3 | 8e-15 | 31/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +8.3 | 1e-14 | 20/48 (C32, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +7.9 | 2e-13 | 24/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.4 | 3e-06 | 18/48 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +5.2 | 1e-05 | 9/48 (SNU-1, RKO, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | 1.16× | +4.9 | 4e-05 | 18/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.16× | +4.8 | 6e-05 | 20/48 (C32, SK-MEL-2, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.19× | +4.1 | 0.002 | 16/49 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.9 | 0.003 | 5/49 (LS 180, KATO III, …) | top dose only |  |
| [[Amsacrine (drug)]] 0.5 µM |  | 1.10× | +3.2 | 0.040 | 3/49 (RKO, A549, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.040 | 11/47 (A-172, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 1.06× | +2.9 | 0.066 | 1/49 (SNU-1) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 1.09× | +2.9 | 0.076 | 5/48 (SNU-1, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4078.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.781×** | -11.5 | 9e-28 | 33/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.815×** | -6.7 | 5e-09 | 23/48 (AN3 CA, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.826×** | -6.0 | 3e-07 | 23/48 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.838× | -5.8 | 8e-07 | 20/49 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -5.6 | 3e-06 | 19/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.806×** | -3.7 | 0.019 | 9/49 (COLO 205, HS-578T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.904× | -3.3 | 0.072 | 10/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.972× | -3.2 | 0.098 | 0/50 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4078. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 67.7 | 7 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +18.2) | — |
| [[HT-29 (line)]] | alt | 68.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.20× (z +10.4) | — |
| [[KATO III (line)]] | alt | 93.8 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.16× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 100 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.38× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 64.6 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +12.6) | — |
| [[NCI-H596 (line)]] | alt | 76.8 | 0 | 3 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.223× (z -11.1) |
| [[A-427 (line)]] | wt | 59.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.26× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.16× (z +8.8) | — |
| [[C32 (line)]] | wt | 69.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +11.0) ⚠ cell-cycle shift, explains ~4% of this change | — |
| [[CFPAC-1 (line)]] | alt | 97.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.411× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 68.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.90× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 104 | 1 | 1 | [[Auranofin (drug)]] 5 µM 1.70× (z +8.7) | [[Tucidinostat (drug)]] 5 µM 0.657× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 91.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +19.2) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[SW480 (line)]] | alt | 49.1 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.76× (z +9.4) | — |
| [[A498 (line)]] | wt | 58.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.5) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[BT-474 (line)]] | alt | 83.9 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.158× (z -11.2) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 79.2 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.361× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 104 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 76.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.76× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 62.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +11.0) | — |
| [[RKO (line)]] | wt | 76.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.37× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | — |
| [[A-172 (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 99.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 88.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 84.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 69.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 91.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4078), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1D]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[EMC3]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[TMUB2]] | +0.58 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[NR1H2]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SNIP1]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[RTF2]] | +0.54 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[LAMTOR3]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[MTPN]] | +0.53 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[CCNK]] | +0.53 | +0.53 / +0.51 | both halves | 1e-05 | pathway: HIV Infection |
| [[BIN3]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PRPF18]] | +0.52 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[VAMP3]] | +0.52 | +0.51 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_PROTEIN_SECRETION |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF592]] | -0.53 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[ASB13]] | -0.50 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[LRRC8B]] | -0.49 | -0.25 / -0.64 | both halves | 4e-04 |  |
| [[GPR63]] | -0.49 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[WDR75]] | -0.47 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[SCML2]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ZNRF2P1]] | -0.46 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[ANGEL1]] | -0.45 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[MTFP1]] | -0.44 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[CEP85]] | -0.44 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ISOC1]] | -0.43 | -0.46 / -0.44 | both halves | 3e-05 | pathway: HALLMARK_PEROXISOME |
| [[PMS1]] | -0.43 | -0.38 / -0.45 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.184). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-27.5, -10.1); signed map (-3.4, -5.5). **Vector** length 107, 26.4% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.7 | +12.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.3 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.7 | +9.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +4.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.3 | -6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.3 | -6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -4.3 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -5.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | vacuolar protein sorting 4 homolog B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33 — chr18:63,389,190-63,422,483 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VPS4-2, SKD1B; previously SKD1 |
| Gene groups (HGNC) | AAA ATPases; ESCRT-IV |
| Hallmark sets | PEROXISOME, PROTEIN_SECRETION |
| Reactome | 8 pathways, smallest: Budding and maturation of HIV virion; Endosomal Sorting Complex Required For Transport (ESCRT); Late Phase of HIV Life Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O75351](https://www.uniprot.org/uniprotkb/O75351) (Vacuolar protein sorting-associated protein 4B):

> Involved in late steps of the endosomal multivesicular bodies (MVB) pathway. Recognizes membrane-associated ESCRT-III assemblies and catalyzes their ATP-dependent disassembly, possibly in combination with membrane fission. Redistributes the ESCRT-III components to the cytoplasm for further rounds of MVB sorting. MVBs contain intraluminal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome and mostly are delivered to lysosomes enabling …

**Summary**, from NCBI Gene [9525](https://www.ncbi.nlm.nih.gov/gene/9525):

> The protein encoded by this gene is a member of the AAA protein family (ATPases associated with diverse cellular activities), and is the homolog of the yeast Vps4 protein. In humans, two paralogs of the yeast protein have been identified. The former share a high degree of aa sequence similarity with each other, and also with yeast Vps4 and mouse Skd1 proteins. Mouse Skd1 (suppressor of K+ transport defect 1) has been shown to be a yeast Vps4 ortholog. Functional studies indicate that both human …

**Accessions** — [HGNC:10895](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10895) · Entrez [9525](https://www.ncbi.nlm.nih.gov/gene/9525) · UniProt [O75351](https://www.uniprot.org/uniprotkb/O75351) · Ensembl [ENSG00000119541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119541)

## Data

Gene col 4078: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4078); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4078, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4078]; `tensor/DDL_lfc|DDL_z.npy` [4078]; `embed/gene_vectors.npy` [4078]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4078 or target_col == 4078). Every well: [[VPS4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
