---
symbol: "SGK3"
type: "gene"
col: 2425
ensembl_id: "ENSG00000104205"
name: "serum/glucocorticoid regulated kinase family member 3"
location: "8q13.1"
module: 40
arm: "+"
pooled_cpm: 39.86
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SGK3

*serum/glucocorticoid regulated kinase family member 3* — 8q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.46× (z +14.1, q 3e-42, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.338× (z -8.9, q 4e-16, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRP54-AS1]] (+0.70, fdr 1e-05), [[RAB6A]] (+0.67, fdr 1e-05), [[ELP2]] (+0.66, fdr 7e-06); moves opposite to [[PURB]] (-0.69, fdr 7e-06), [[TASOR]] (-0.66, fdr 1e-05), [[CSTF2T]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2425.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.46×** | +14.1 | 3e-42 | 46/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.18×** | +12.2 | 1e-31 | 41/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +9.3 | 4e-18 | 37/47 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +8.7 | 6e-16 | 30/47 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +8.5 | 2e-15 | 38/47 (HS-578T, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +6.4 | 1e-08 | 28/47 (SHP-77, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +5.9 | 4e-07 | 30/47 (HOP62, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.8 | 1e-04 | 23/46 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +4.2 | 0.001 | 20/47 (PANC-1, HS-578T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.006 | 19/47 (A498, NCI-H2030, …) | top dose only |  |
| [[Brivudine (drug)]] 0.5 µM |  | 1.32× | +3.1 | 0.10 | 16/47 (SHP-77, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.13 | 11/47 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2425.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.338×** | -8.9 | 4e-16 | 39/48 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.687×** | -5.6 | 5e-06 | 30/46 (A498, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.718×** | -5.2 | 4e-05 | 27/47 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.722×** | -4.7 | 4e-04 | 21/40 (SW 900, RPMI-7951, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.752×** | -4.1 | 0.004 | 22/46 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.612×** | -4.0 | 0.005 | 21/46 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.774×** | -4.0 | 0.005 | 17/47 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.781×** | -3.9 | 0.008 | 20/45 (RKO, NCI-H2347, …) | inconsistent across doses | composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | **0.787×** | -3.7 | 0.011 | 17/47 (SNU-423, CFPAC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.839× | -3.6 | 0.019 | 13/47 (SNU-423, NCI-H460, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | **0.804×** | -3.4 | 0.034 | 24/45 (A498, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.806×** | -3.4 | 0.036 | 18/47 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.816×** | -3.2 | 0.064 | 11/47 (SW 1088, SNU-423, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.819×** | -3.1 | 0.076 | 18/47 (HT-29, SW 1088, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.821×** | -3.1 | 0.077 | 10/47 (SW 900, NCI-H2347, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.816×** | -3.0 | 0.077 | 15/47 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.825×** | -3.0 | 0.083 | 15/47 (SW 1088, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2425. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 49.1 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.78× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 25.1 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +13.9) | — |
| [[A549 (line)]] | wt | 28.2 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 30.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.55× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.330× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[PANC-1 (line)]] | alt | 41.2 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.94× (z +12.8) | [[Pralsetinib (drug)]] 5 µM 0.249× (z -8.6) |
| [[HS-578T (line)]] | alt | 46.3 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.36× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 77.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.192× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 22.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.94× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 21.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.107× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 68.4 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0903× (z -22.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 75.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.75× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -15.8) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.70× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 72.3 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.94× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.140× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 55.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[H4 (line)]] | wt | 31.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[HCT15 (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LoVo (line)]] | wt | 39.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.30× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 45.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -9.3) |
| [[SW480 (line)]] | alt | 34.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.57× (z +9.6) | — |
| [[A-172 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.52 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2425), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54-AS1]] | +0.70 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[RAB6A]] | +0.67 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ELP2]] | +0.66 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[KCTD7]] | +0.66 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TMEM50B]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[MAX]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[PIK3C2A]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SEC11A]] | +0.63 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SCAI]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.61 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[SLC17A5]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[AKR1A1]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PURB]] | -0.69 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[TASOR]] | -0.66 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[CSTF2T]] | -0.64 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.64 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[ZNF268]] | -0.64 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[PUF60]] | -0.63 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[SRCAP]] | -0.63 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[MED1]] | -0.63 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[ZNF629]] | -0.62 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[TAF2]] | -0.61 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ZNF614]] | -0.61 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ZC3H4]] | -0.61 | -0.51 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SGK3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SGK3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-37.4, 16.4); signed map (-42.6, 13.0). **Vector** length 103, 25.6% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +12.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +3.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.3 | -8.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -6.0 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.4 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.0 | -5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -2.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.8 | -3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | serum/glucocorticoid regulated kinase family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.1 — chr8:66,712,734-66,862,022 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SGK2, SGKL |
| Gene groups (HGNC) | Serum/glucocorticoid regulated kinase family |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BR1](https://www.uniprot.org/uniprotkb/Q96BR1) (Serine/threonine-protein kinase Sgk3):

> Serine/threonine-protein kinase which is involved in the regulation of a wide variety of ion channels, membrane transporters, cell growth, proliferation, survival and migration. Up-regulates Na(+) channels: SCNN1A/ENAC and SCN5A, K(+) channels: KCNA3/KV1.3, KCNE1, KCNQ1 and KCNH2/HERG, epithelial Ca(2+) channels: TRPV5 and TRPV6, chloride channel: BSND, creatine transporter: SLC6A8, Na(+)/dicarboxylate cotransporter: SLC13A2/NADC1, Na(+)-dependent phosphate cotransporter: SLC34A2/NAPI-2B, amino …

**Summary**, from NCBI Gene [23678](https://www.ncbi.nlm.nih.gov/gene/23678):

> This gene is a member of the Ser/Thr protein kinase family and encodes a phosphoprotein with a PX (phox homology) domain. The protein phosphorylates several target proteins and has a role in neutral amino acid transport and activation of potassium and chloride channels. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10812) · Entrez [23678](https://www.ncbi.nlm.nih.gov/gene/23678) · UniProt [Q96BR1](https://www.uniprot.org/uniprotkb/Q96BR1) · Ensembl [ENSG00000104205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104205)

## Data

Gene col 2425: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2425); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2425, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2425]; `tensor/DDL_lfc|DDL_z.npy` [2425]; `embed/gene_vectors.npy` [2425]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2425 or target_col == 2425). Every well: [[SGK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
