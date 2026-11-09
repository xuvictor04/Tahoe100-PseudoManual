---
symbol: "DBNL"
type: "gene"
col: 5851
ensembl_id: "ENSG00000136279"
name: "drebrin like"
location: "7p13"
module: 111
arm: "+"
pooled_cpm: 30.12
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# DBNL

*drebrin like* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.46× (z +13.0, q 1e-35, up in 34 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.33× (z +6.0, q 2e-07, up in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A498 3.89×, PANC-1 3.23×, NCI-H1792 3.94×, LOX-IMVI 3.40×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A498 3.17×, SNU-423 4.89×, PANC-1 2.86×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 3.68×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.561× (z -8.6, q 3e-15, down in 37 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.610× (z -7.4, q 4e-11, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR1]] (+0.69, fdr 1e-05), [[ARPC4]] (+0.67, fdr 1e-05), [[ACTR3]] (+0.66, fdr 1e-05); moves opposite to [[ATP5MC2]] (-0.68, fdr 1e-05), [[C15orf61]] (-0.65, fdr 1e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[LSM2]] (-0.63, fdr 7e-06), [[MRPL34]] (-0.63, fdr 2e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5851.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A498 3.89×, PANC-1 3.23×, NCI-H1792 3.94×, LOX-IMVI 3.40×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A498 3.17×, SNU-423 4.89×, PANC-1 2.86×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 3.68×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +13.0 | 1e-35 | 34/35 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +11.4 | 8e-28 | 32/38 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +8.9 | 1e-16 | 35/44 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.0 | 2e-07 | 28/48 (A498, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.37×** | +4.8 | 2e-04 | 23/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.4 | 0.057 | 1/48 (CHP-212) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.085 | 10/48 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.24×** | +3.2 | 0.085 | 13/46 (NCI-H2347, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.24× | +3.1 | 0.10 | 18/48 (A498, NCI-H460, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.1 | 0.10 | 7/48 (A498, RPMI-7951, …) | top dose only |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 1.24× | +3.0 | 0.13 | 10/48 (HS-578T, KATO III, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5851.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -8.6 | 3e-15 | 37/47 (KATO III, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.610×** | -7.4 | 4e-11 | 35/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.623×** | -7.1 | 3e-10 | 42/48 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.665×** | -6.1 | 2e-07 | 33/48 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.731×** | -4.7 | 3e-04 | 29/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.793×** | -3.5 | 0.053 | 18/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.797×** | -3.4 | 0.058 | 18/47 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 34.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +12.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 23.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.40× (z +8.6) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.219× (z -11.1) |
| [[COLO 205 (line)]] | alt | 41.8 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.192× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 17.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.94× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -14.4) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 25.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 28.9 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~6% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.151× (z -10.2) |
| [[A-427 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.250× (z -10.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 54.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +8.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.461× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -14.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 25.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.270× (z -11.2) |
| [[LS 180 (line)]] | wt | 24.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.197× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.89× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 31.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR1]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 | same gene group; STRING 478 |
| [[ARPC4]] | +0.67 | +0.50 / +0.67 | both halves | 1e-05 | STRING 449 |
| [[ACTR3]] | +0.66 | +0.50 / +0.66 | both halves | 1e-05 | STRING 673 |
| [[SF3B4]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SNX19]] | +0.64 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[CEP170B]] | +0.64 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[AP1B1]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 | same gene group |
| [[UBA1]] | +0.63 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[FLNA]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[HIGD1A]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[CDC42]] | +0.61 | +0.38 / +0.66 | both halves | 6e-05 | STRING 537 |
| [[EXOC7]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*38 of its nearest partners move opposite, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MC2]] | -0.68 | -0.53 / -0.70 | both halves | 1e-05 |  |
| [[C15orf61]] ⚠ | -0.65 | -0.50 / -0.67 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LSM2]] | -0.63 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[MRPL34]] | -0.63 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[NACA4P]] ⚠ | -0.62 | -0.42 / -0.64 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRIM52-AS1]] | -0.60 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[DPM3]] | -0.59 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[SNHG7]] | -0.59 | -0.31 / -0.67 | both halves | 2e-04 |  |
| [[AFMID]] | -0.58 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.58 | -0.30 / -0.61 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CAMLG]] | -0.58 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[RPS27A]] ⚠ | -0.57 | -0.40 / -0.62 | both halves | 5e-05 | pathway: Apoptosis; ⚠ in the vector space only through flagged drug-doses |
| [[SNHG19]] | -0.57 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[TAF1D]] | -0.57 | -0.36 / -0.63 | both halves | 1e-04 |  |
| [[TOMM7]] | -0.57 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[LAMTOR5]] | -0.56 | -0.37 / -0.58 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.5, -19.3); signed map (-7.9, 34.0). **Vector** length 96.8, 22.1% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *RHO GTPase Effectors* (reactome, mean cos +0.51 to 10); *EPHB-mediated forward signaling* (reactome, mean cos +0.51 to 6); *Leishmania infection* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +13.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +6.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | -0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +1.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -2.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -0.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -8.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.7 | -0.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.1 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | drebrin like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,044,640-44,069,456 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SH3P7, HIP-55, ABP1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Drebrin family; SH3 domain containing |
| Reactome | 10 pathways, smallest: Caspase-mediated cleavage of cytoskeletal proteins; Apoptotic cleavage of cellular proteins; Neurexins and neuroligins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJU6](https://www.uniprot.org/uniprotkb/Q9UJU6) (Drebrin-like protein):

> Adapter protein that binds F-actin and DNM1, and thereby plays a role in receptor-mediated endocytosis. Plays a role in the reorganization of the actin cytoskeleton, formation of cell projections, such as neurites, in neuron morphogenesis and synapse formation via its interaction with WASL and COBL. Does not bind G-actin and promote actin polymerization by itself. Required for the formation of organized podosome rosettes (By similarity). May act as a common effector of antigen …

**Summary**, from NCBI Gene [28988](https://www.ncbi.nlm.nih.gov/gene/28988):

> Enables cadherin binding activity. Predicted to be involved in several processes, including Rac protein signal transduction; nervous system development; and podosome assembly. Located in cytoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:2696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2696) · Entrez [28988](https://www.ncbi.nlm.nih.gov/gene/28988) · UniProt [Q9UJU6](https://www.uniprot.org/uniprotkb/Q9UJU6) · Ensembl [ENSG00000136279](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136279)

## Data

Gene col 5851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5851); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5851]; `tensor/DDL_lfc|DDL_z.npy` [5851]; `embed/gene_vectors.npy` [5851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5851 or target_col == 5851). Every well: [[DBNL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DBNL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
