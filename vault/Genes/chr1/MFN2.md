---
symbol: "MFN2"
type: "gene"
col: 3822
ensembl_id: "ENSG00000116688"
name: "mitofusin 2"
location: "1p36.22"
module: 25
arm: "+"
pooled_cpm: 37.55
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# MFN2

*mitofusin 2* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.68× (z +10.8, q 1e-24, up in 33 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.54× (z +9.0, q 3e-17, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.761× (z -8.1, q 4e-13, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Orlistat (drug)]] 0.05 µM in 1 line (AN3 CA 0.102×); [[Lonafarnib (drug)]] 5 µM in 1 line (C32 0.0998×; ⚠ toxic); [[Radotinib (drug)]] 0.5 µM in 1 line (H4 0.234×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA10]] (+0.73, fdr 7e-06), [[PSME3]] (+0.72, fdr 7e-06), [[PCNX3]] (+0.71, fdr 7e-06); moves opposite to [[TCAF1]] (-0.62, fdr 3e-05), [[TMEM191A-1]] (-0.62, fdr 3e-05), [[SMIM26]] (-0.61, fdr 3e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[PIM3]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3822.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +10.8 | 1e-24 | 33/45 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +10.4 | 8e-23 | 33/40 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +9.0 | 3e-17 | 36/48 (HT-29, HCT15, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +6.9 | 7e-10 | 29/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +6.8 | 1e-09 | 28/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.25×** | +6.6 | 3e-09 | 22/47 (SNU-1, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +6.6 | 3e-09 | 33/48 (RKO, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +6.0 | 2e-07 | 32/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +5.4 | 4e-06 | 25/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +5.2 | 1e-05 | 24/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +5.1 | 2e-05 | 24/48 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.29×** | +5.0 | 3e-05 | 19/42 (HOP62, Hs 766T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +4.5 | 3e-04 | 19/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.4 | 4e-04 | 0/48 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.21×** | +3.8 | 0.006 | 21/47 (LoVo, HOP62, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.033 | 10/48 (Hs 766T, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.3 | 0.033 | 9/48 (SW480, SNU-1, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.055 | 10/47 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.058 | 9/48 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 1.16× | +2.9 | 0.090 | 6/48 (LOX-IMVI, HEC-1-A, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3822.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Orlistat (drug)]] 0.05 µM in 1 line (AN3 CA 0.102×); [[Lonafarnib (drug)]] 5 µM in 1 line (C32 0.0998×; ⚠ toxic); [[Radotinib (drug)]] 0.5 µM in 1 line (H4 0.234×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.761×** | -8.1 | 4e-13 | 35/48 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.731×** | -6.6 | 2e-08 | 33/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.4 | 0.10 | 12/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.851× | -3.4 | 0.10 | 13/47 (HepG2/C3A, A-427, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.864× | -3.1 | 0.24 | 11/48 (LoVo, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3822. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 47.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Lonafarnib (drug)]] 5 µM 0.0998× (z -9.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 21.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 43.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +11.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 52.4 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.102× (z -10.1) |
| [[H4 (line)]] | wt | 37.5 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.234× (z -8.7) |
| [[HCT15 (line)]] | alt | 39.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 32.5 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.00× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 46.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 43.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +8.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 31.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 35.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 28.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 47.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.13× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 42.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3822), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA10]] | +0.73 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[PSME3]] | +0.72 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[PCNX3]] | +0.71 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[GCN1]] | +0.71 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.70 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[STX16]] | +0.69 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[LY6G5B]] | +0.69 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[TBL3]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[SSU72]] | +0.68 | +0.57 / +0.72 | both halves | 9e-06 |  |
| [[HCFC1]] | +0.68 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[U2AF2]] | +0.67 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[MCM3AP]] | +0.66 | +0.51 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCAF1]] | -0.62 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[TMEM191A-1]] | -0.62 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[SMIM26]] ⚠ | -0.61 | -0.43 / -0.62 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PIM3]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[UGCG]] | -0.61 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[IFI27L2]] | -0.61 | -0.33 / -0.66 | both halves | 1e-04 |  |
| [[MARCHF9]] | -0.59 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[RPL18]] ⚠ | -0.59 | -0.38 / -0.64 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BTG1]] | -0.58 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[RAB9A]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[CHMP2B]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 | pathway: Autophagy |
| [[RPL36AL]] ⚠ | -0.57 | -0.42 / -0.59 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NBPF14]] | -0.57 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[SUMO4]] | -0.57 | -0.22 / -0.65 | both halves | 6e-04 |  |
| [[IMP3]] | -0.56 | -0.35 / -0.61 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.4, -27.5); signed map (-14.7, -32.5). **Vector** length 86.0, 17.2% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +6.0 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +9.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +3.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -6.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.0 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | mitofusin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,980,181-12,015,211 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CPRP1, KIAA0214, MARF, CMT2A2 |
| Gene groups (HGNC) | Mitofusin family |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 10 pathways, smallest: RHOT2 GTPase cycle; Miro GTPase Cycle; PINK1-PRKN Mediated Mitophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [O95140](https://www.uniprot.org/uniprotkb/O95140) (Mitofusin-2):

> Mitochondrial outer membrane GTPase that mediates mitochondrial clustering and fusion. Mitochondria are highly dynamic organelles, and their morphology is determined by the equilibrium between mitochondrial fusion and fission events. Overexpression induces the formation of mitochondrial networks. Membrane clustering requires GTPase activity and may involve a major rearrangement of the coiled coil domains (Probable). Plays a central role in mitochondrial metabolism and may be associated with …

**Summary**, from NCBI Gene [9927](https://www.ncbi.nlm.nih.gov/gene/9927):

> This gene encodes a mitochondrial membrane protein that participates in mitochondrial fusion and contributes to the maintenance and operation of the mitochondrial network. This protein is involved in the regulation of vascular smooth muscle cell proliferation, and it may play a role in the pathophysiology of obesity. Mutations in this gene cause Charcot-Marie-Tooth disease type 2A2, and hereditary motor and sensory neuropathy VI, which are both disorders of the peripheral nervous system. …

**Accessions** — [HGNC:16877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16877) · Entrez [9927](https://www.ncbi.nlm.nih.gov/gene/9927) · UniProt [O95140](https://www.uniprot.org/uniprotkb/O95140) · Ensembl [ENSG00000116688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116688)

## Data

Gene col 3822: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3822); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3822, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3822]; `tensor/DDL_lfc|DDL_z.npy` [3822]; `embed/gene_vectors.npy` [3822]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3822 or target_col == 3822). Every well: [[MFN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
