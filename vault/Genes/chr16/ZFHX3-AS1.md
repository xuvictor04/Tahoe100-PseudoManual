---
symbol: "ZFHX3-AS1"
type: "gene"
col: 15233
ensembl_id: "ENSG00000259768"
name: "ZFHX3 antisense RNA 1"
location: "16q22.2"
module: 91
arm: "+"
pooled_cpm: 38.03
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# ZFHX3-AS1

*ZFHX3 antisense RNA 1* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.07× (z +12.7, q 5e-34, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 1.63× (z +4.5, q 7e-04, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.478× (z -12.7, q 2e-34, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01572]] (+0.77, fdr 7e-06, ⚠ same locus), [[KIF24]] (+0.76, fdr 7e-06), [[ZGRF1]] (+0.76, fdr 7e-06), [[BRCA2]] (+0.70, fdr 7e-06).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15233.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.07×** | +12.7 | 5e-34 | 43/48 (A498, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.87×** | +10.9 | 2e-25 | 43/48 (A498, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.71×** | +9.4 | 1e-18 | 40/48 (A498, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.39×** | +5.2 | 2e-05 | 26/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +5.1 | 4e-05 | 21/48 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +4.5 | 7e-04 | 19/48 (KATO III, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | 1.19× | +4.0 | 0.006 | 12/48 (HEC-1-A, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.26×** | +3.8 | 0.012 | 17/48 (SW480, SW1417, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.025 | 12/48 (LS 180, KATO III, …) | two highest doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.031 | 9/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.15× | +3.4 | 0.032 | 12/48 (A-427, HOP62, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.052 | 10/48 (KATO III, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Brimonidine (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.054 | 6/48 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.068 | 14/48 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | 1.20× | +3.1 | 0.068 | 15/48 (RKO, HOP62, …) | all doses, flat |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.13× | +3.1 | 0.071 | 6/48 (NCI-H661, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.0 | 0.084 | 13/48 (LS 180, KATO III, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.478×** | -12.7 | 2e-34 | 42/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.549×** | -10.3 | 1e-22 | 40/48 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.550×** | -10.3 | 1e-22 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.613×** | -8.4 | 5e-15 | 30/48 (PANC-1, AN3 CA, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.617×** | -8.3 | 1e-14 | 33/47 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.609×** | -8.1 | 7e-14 | 31/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.639×** | -7.0 | 2e-10 | 29/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.692×** | -6.3 | 2e-08 | 29/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.774×** | -6.2 | 4e-08 | 29/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.706×** | -5.8 | 4e-07 | 30/48 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.548×** | -5.4 | 3e-06 | 24/42 (SNU-423, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.551×** | -5.4 | 4e-06 | 23/48 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.757×** | -4.8 | 8e-05 | 18/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.591×** | -4.7 | 9e-05 | 22/48 (HEC-1-A, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.608×** | -4.5 | 3e-04 | 17/30 (LOX-IMVI, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.722×** | -4.0 | 0.002 | 17/48 (A-427, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.796×** | -3.8 | 0.005 | 12/47 (SK-MEL-2, SW48, …) | two highest doses |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.806×** | -3.7 | 0.007 | 15/48 (SW 1271, HOP62, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.811×** | -3.6 | 0.010 | 17/48 (MIA PaCa-2, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 99.0 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.146× (z -20.7) |
| [[PANC-1 (line)]] | alt | 35.8 | 0 | 8 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.177× (z -18.2) |
| [[A-427 (line)]] | wt | 56.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.129× (z -10.2) |
| [[KATO III (line)]] | alt | 42.6 | 3 (3 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 2.60× (z +9.0) ⚠ cell-cycle shift, explains ~48% of this change | [[Digitoxin (drug)]] 0.5 µM 0.292× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 75.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 34.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.43× (z +11.3) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[HCT15 (line)]] | alt | 47.5 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.263× (z -9.2) |
| [[J82 (line)]] | alt | 37.1 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.290× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 51.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.286× (z -9.5) |
| [[SW48 (line)]] | wt | 23.3 | 0 | 2 (1 ⚠) | — | [[Monocrotaline (drug)]] 0.05 µM 0.0640× (z -11.3) |
| [[A-172 (line)]] | wt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -9.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0665× (z -11.4) |
| [[CHP-212 (line)]] | wt | 38.7 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.5 µM 0.0592× (z -11.5) |
| [[COLO 205 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 61.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.372× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 39.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 29.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.375× (z -9.1) |
| [[RKO (line)]] | wt | 31.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 44.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.301× (z -9.0) |
| [[SNU-423 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0670× (z -9.6) ⚠ toxic |
| [[A549 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01572]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[KIF24]] | +0.76 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[ZGRF1]] | +0.76 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[BRCA2]] | +0.70 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[BRCA1]] | +0.70 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[BRIP1]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[WDHD1]] | +0.68 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[SKA3]] | +0.68 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[PLK4]] | +0.68 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[RFC2]] | +0.67 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[ESCO2]] | +0.67 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[SMC2]] | +0.67 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[HROB]] | +0.66 | +0.51 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-38.8, -49.0); signed map (-43.0, -46.1). **Vector** length 89.7, 22.9% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.56 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.60 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.60 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +2.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.7 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.6 | +1.7 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | +1.4 | +2.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -6.0 | -8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.1 | -12.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.4 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.2 | +3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.9 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -8.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ZFHX3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16q22.2 — chr16:72,665,123-72,828,293 (+) |
| Ensembl biotype | lncRNA |
| Also known as | AC004943.2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56033](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56033) · Entrez [101927978](https://www.ncbi.nlm.nih.gov/gene/101927978) · Ensembl [ENSG00000259768](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259768)

## Data

Gene col 15233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15233); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15233]; `tensor/DDL_lfc|DDL_z.npy` [15233]; `embed/gene_vectors.npy` [15233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15233 or target_col == 15233). Every well: [[ZFHX3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFHX3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
