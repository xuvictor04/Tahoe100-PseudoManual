---
symbol: "SPSB3"
type: "gene"
col: 8471
ensembl_id: "ENSG00000162032"
name: "splA/ryanodine receptor domain and SOCS box containing 3"
location: "16p13.3"
module: 76
arm: "+"
pooled_cpm: 11.72
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# SPSB3

*splA/ryanodine receptor domain and SOCS box containing 3* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.67× (z +11.1, q 7e-26, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.196× (z -18.4, q 0e+00, down in 46 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.483× (z -7.9, q 1e-12, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01881]] (+0.82, fdr 7e-06), [[WIPI2]] (+0.77, fdr 7e-06), [[MAP3K3]] (+0.74, fdr 7e-06); moves opposite to [[NCR3LG1]] (-0.63, fdr 1e-05), [[UTP20]] (-0.61, fdr 1e-05), [[ENOSF1]] (-0.61, fdr 3e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.67×** | +11.1 | 7e-26 | 44/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +10.0 | 6e-21 | 44/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.24×** | +9.2 | 1e-17 | 42/47 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +4.7 | 4e-04 | 20/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.05×** | +4.6 | 5e-04 | 19/43 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.90×** | +4.1 | 0.003 | 21/44 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.75×** | +3.6 | 0.025 | 11/44 (HEC-1-A, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.4 | 0.046 | 19/38 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.35×** | +3.4 | 0.046 | 11/42 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +3.3 | 0.054 | 6/43 (HCT15, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.61× | +3.1 | 0.11 | 7/44 (LS 180, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8471.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.196×** | -18.4 | 0e+00 | 46/47 (A498, SK-MEL-2, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.483×** | -7.9 | 1e-12 | 32/46 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.621×** | -7.6 | 7e-12 | 28/45 (AsPC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.506×** | -7.2 | 6e-11 | 35/46 (A498, Hs 766T, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.247×** | -7.2 | 1e-10 | 31/42 (SW480, A498, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.260×** | -6.9 | 5e-10 | 32/44 (AsPC-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.273×** | -6.6 | 3e-09 | 35/44 (A498, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.275×** | -6.6 | 3e-09 | 35/43 (Panc 03.27, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.281×** | -6.5 | 5e-09 | 34/45 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.431×** | -5.4 | 5e-06 | 29/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.625×** | -5.3 | 6e-06 | 28/46 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.686×** | -4.2 | 0.001 | 21/44 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.768×** | -4.2 | 0.001 | 20/48 (A498, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.692×** | -4.1 | 0.002 | 15/46 (AsPC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.779×** | -3.9 | 0.003 | 21/48 (HCT15, Hs 766T, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.696×** | -3.8 | 0.004 | 16/48 (CFPAC-1, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 25.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -15.8) |
| [[A498 (line)]] | wt | 26.8 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0989× (z -15.7) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.230× (z -9.6) |
| [[HS-578T (line)]] | alt | 15.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0840× (z -13.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.173× (z -13.2) |
| [[A-172 (line)]] | wt | 15.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 7.34 | 0 | 2 (2 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.0860× (z -9.9) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 9.13 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0406× (z -11.5) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.172× (z -10.4) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.145× (z -9.5) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 9.90 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.167× (z -9.4) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 8.12 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0837× (z -10.3) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 7.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 8.83 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.239× (z -8.7) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 5.90 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.182× (z -9.2) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.230× (z -9.2) |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.161× (z -8.6) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 9.75 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.165× (z -8.5) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.198× (z -9.5) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 9.36 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.220× (z -9.6) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01881]] | +0.82 | +0.70 / +0.80 | both halves | 7e-06 |  |
| [[WIPI2]] | +0.77 | +0.68 / +0.85 | both halves | 7e-06 |  |
| [[MAP3K3]] | +0.74 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[RAB40B]] | +0.73 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[LCMT1]] | +0.73 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[CCDC28A]] | +0.72 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[MXD4]] | +0.72 | +0.67 / +0.82 | both halves | 7e-06 |  |
| [[MPST]] | +0.71 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MIGA2]] | +0.71 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ABTB1]] | +0.71 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[NUBP2]] | +0.71 | +0.65 / +0.57 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ULK1]] | +0.71 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[MACO1]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCR3LG1]] | -0.63 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[UTP20]] | -0.61 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[ENOSF1]] | -0.61 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ZNF300]] | -0.61 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[SLC16A9]] | -0.59 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ZNF462]] | -0.59 | -0.56 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.847). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.2, -44.3); signed map (-20.0, 11.0). **Vector** length 111, 28.8% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.3 | +10.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.2 | +11.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.1 | +9.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.8 | +4.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.8 | +4.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.4 | +4.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.3 | +3.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.9 | -18.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.7 | -6.6 |
|  | [[EX229 (drug)]] 5 µM |  | -6.6 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.4 | -6.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.0 | -6.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.0 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | splA/ryanodine receptor domain and SOCS box containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,776,712-1,793,700 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SSB-3; previously C16orf31 |
| Gene groups (HGNC) | SplA/ryanodine receptor domain and SOCS box containing family |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PJ21](https://www.uniprot.org/uniprotkb/Q6PJ21) (SPRY domain-containing SOCS box protein 3):

> Substrate-recognition component of a cullin-5-RING E3 ubiquitin-protein ligase complex (ECS complex, also named CRL5 complex), which mediates the ubiquitination and subsequent proteasomal degradation of target proteins, such as CGAS and SNAI1. The ECS(SPSB3) complex catalyzes 'Lys-48'-linked ubiquitination of nuclear CGAS in cycling cells, leading to its degradation. Recognizes and binds nucleosome-bound CGAS: ubiquitination and degradation of nuclear CGAS during G1 and G2 phases is required to …

**Summary**, from NCBI Gene [90864](https://www.ncbi.nlm.nih.gov/gene/90864):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in several processes, including negative regulation of cGAS/STING signaling pathway; negative regulation of epithelial to mesenchymal transition; and protein K48-linked ubiquitination. Part of Cul5-RING ubiquitin ligase complex. Is active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30629) · Entrez [90864](https://www.ncbi.nlm.nih.gov/gene/90864) · UniProt [Q6PJ21](https://www.uniprot.org/uniprotkb/Q6PJ21) · Ensembl [ENSG00000162032](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162032)

## Data

Gene col 8471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8471); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8471]; `tensor/DDL_lfc|DDL_z.npy` [8471]; `embed/gene_vectors.npy` [8471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8471 or target_col == 8471). Every well: [[SPSB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPSB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
