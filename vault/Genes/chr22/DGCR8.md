---
symbol: "DGCR8"
type: "gene"
col: 4863
ensembl_id: "ENSG00000128191"
name: "DGCR8 microprocessor complex subunit"
location: "22q11.21"
module: 71
arm: "+"
pooled_cpm: 27.08
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# DGCR8

*DGCR8 microprocessor complex subunit* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.11× (z +6.1, q 5e-07, up in 2 of 48 measured lines) ⚠ position not correctable.
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.492× (z -11.6, q 1e-28, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCA]] (+0.71, fdr 7e-06), [[TRAPPC10]] (+0.70, fdr 7e-06), [[AUNIP]] (+0.70, fdr 1e-05); moves opposite to [[SDCBP]] (-0.61, fdr 1e-05), [[SGO1-AS1]] (-0.57, fdr 1e-05), [[CLCN3]] (-0.57, fdr 1e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +6.1 | 5e-07 | 2/48 (HCT15, COLO 205) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +5.8 | 2e-06 | 27/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.21× | +3.2 | 0.20 | 14/47 (SW480, HCT15, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.20 | 15/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | 1.21× | +3.1 | 0.20 | 11/45 (SW480, HCT15, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.20 | 16/47 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +3.0 | 0.21 | 8/48 (BT-474, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4863.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.492×** | -11.6 | 1e-28 | 36/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.626×** | -11.3 | 4e-27 | 36/47 (C32, A-172, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.738×** | -7.3 | 3e-11 | 30/48 (SNU-1, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.650×** | -7.3 | 3e-11 | 25/42 (NCI-H2030, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.673×** | -6.7 | 2e-09 | 32/48 (Hs 766T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.687×** | -5.9 | 3e-07 | 22/39 (HEC-1-A, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.706×** | -5.7 | 8e-07 | 24/46 (J82, SHP-77, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.789×** | -5.7 | 8e-07 | 25/48 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.708×** | -5.7 | 1e-06 | 22/36 (MIA PaCa-2, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.769×** | -4.5 | 4e-04 | 19/48 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.774×** | -4.4 | 6e-04 | 22/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.805×** | -3.7 | 0.010 | 21/47 (HS-578T, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **0.805×** | -3.7 | 0.010 | 14/48 (COLO 205, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.826×** | -3.3 | 0.045 | 15/48 (LS 180, SW 1271, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -3.2 | 0.052 | 18/48 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 39.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -20.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.103× (z -15.4) |
| [[A-172 (line)]] | wt | 21.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -14.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.154× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 36.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0523× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -11.7) |
| [[A498 (line)]] | wt | 24.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -12.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.256× (z -11.0) |
| [[HS-578T (line)]] | alt | 35.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -15.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.241× (z -11.2) |
| [[A-427 (line)]] | wt | 24.6 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0797× (z -18.1) |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 2 (1 ⚠) | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0751× (z -9.6) |
| [[HOP62 (line)]] | alt | 23.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -12.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.270× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0760× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 24.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -13.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.228× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 23.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -11.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.258× (z -9.1) |
| [[SW48 (line)]] | wt | 45.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -8.7) |
| [[A549 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -9.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.283× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~92% of this change |
| [[HepG2_C3A (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0777× (z -12.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -9.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.277× (z -10.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -11.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -10.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 35.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.266× (z -10.1) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 28.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.230× (z -10.9) |
| [[SW1417 (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -10.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCA]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[TRAPPC10]] | +0.70 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[AUNIP]] | +0.70 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[RAD51]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR |
| [[NDOR1]] | +0.68 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[TRAIP]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[NUP93]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[HIRA]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[TONSL]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 | same gene group |
| [[ZBED4]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ZNF767P-1]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[NUP85]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP]] | -0.61 | -0.62 / -0.55 | both halves | 1e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[SGO1-AS1]] | -0.57 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[CLCN3]] | -0.57 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[CHD2]] | -0.56 | -0.43 / -0.58 | both halves | 3e-05 | same gene group |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.8, -46.6); signed map (-46.0, -21.3). **Vector** length 104, 24.0% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | +5.5 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.0 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -7.4 | -11.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.0 | -7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.8 | -11.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.7 | -6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -5.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | DGCR8 microprocessor complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,080,221-20,111,877 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DGCRK6, Gy1, pasha; previously C22orf12 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Microprocessor complex |
| Hallmark sets | DNA_REPAIR |
| Reactome | 3 pathways, smallest: MicroRNA (miRNA) biogenesis; Transcriptional Regulation by MECP2; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYQ5](https://www.uniprot.org/uniprotkb/Q8WYQ5) (Microprocessor complex subunit DGCR8):

> Component of the microprocessor complex that acts as a RNA- and heme-binding protein that is involved in the initial step of microRNA (miRNA) biogenesis. Component of the microprocessor complex that is required to process primary miRNA transcripts (pri-miRNAs) to release precursor miRNA (pre-miRNA) in the nucleus. Within the microprocessor complex, DGCR8 function as a molecular anchor necessary for the recognition of pri-miRNA at dsRNA-ssRNA junction and directs DROSHA to cleave 11 bp away form …

**Summary**, from NCBI Gene [54487](https://www.ncbi.nlm.nih.gov/gene/54487):

> This gene encodes a subunit of the microprocessor complex which mediates the biogenesis of microRNAs from the primary microRNA transcript. The encoded protein is a double-stranded RNA binding protein that functions as the non-catalytic subunit of the microprocessor complex. This protein is required for binding the double-stranded RNA substrate and facilitates cleavage of the RNA by the ribonuclease III protein, Drosha. Alternate splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:2847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2847) · Entrez [54487](https://www.ncbi.nlm.nih.gov/gene/54487) · UniProt [Q8WYQ5](https://www.uniprot.org/uniprotkb/Q8WYQ5) · Ensembl [ENSG00000128191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128191)

## Data

Gene col 4863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4863); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4863]; `tensor/DDL_lfc|DDL_z.npy` [4863]; `embed/gene_vectors.npy` [4863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4863 or target_col == 4863). Every well: [[DGCR8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGCR8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
