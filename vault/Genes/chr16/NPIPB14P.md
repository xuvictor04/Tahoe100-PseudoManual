---
symbol: "NPIPB14P"
type: "gene"
col: 13519
ensembl_id: "ENSG00000226232"
name: "nuclear pore complex interacting protein family member B14, pseudogene"
location: "16q22.1"
module: 56
arm: "+"
pooled_cpm: 27.16
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 40
n_dd_up_clean: 6
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# NPIPB14P

*nuclear pore complex interacting protein family member B14, pseudogene* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Entecavir (monohydrate) (drug)]] 5 µM: 1.48× (z +5.7, q 5e-06, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (19 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.405× (z -13.4, q 6e-38, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDXDC2P-NPIPB14P]] (+0.81, fdr 7e-06, ⚠ same locus), [[PDXDC1]] (+0.75, fdr 7e-06), [[PDXDC2P]] (+0.71, fdr 7e-06, ⚠ same locus), [[GOLGA2]] (+0.67, fdr 7e-06), [[HYPK]] (+0.65, fdr 7e-06); moves opposite to [[CEBPZOS]] (-0.52, fdr 3e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SMARCA2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PDXDC2P-NPIPB14P]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13519.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **1.48×** | +5.7 | 5e-06 | 27/48 (AsPC-1, C-33 A, …) | rises with dose | plate-row cell shift; position effect removed |
| [[PF-06260933 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +5.2 | 3e-05 | 31/48 (SW 1088, HOP62, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.2 | 3e-05 | 3/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.034 | 10/48 (SW1417, A498, …) | inconsistent across doses | position effect removed |
| [[Berbamine (drug)]] 5 µM |  | 1.18× | +3.6 | 0.034 | 12/48 (NCI-H2347, SHP-77, …) | top dose only | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.044 | 12/48 (AsPC-1, LS 180, …) | top dose only | plate-row cell shift |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.073 | 10/48 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.091 | 13/48 (HEC-1-A, HT-29, …) | top dose only | position effect removed |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.098 | 6/48 (A-172, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 22 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13519.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.405×** | -13.4 | 6e-38 | 42/47 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.461×** | -11.7 | 5e-29 | 34/48 (H4, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.473×** | -10.8 | 4e-25 | 38/47 (A498, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.491×** | -10.7 | 1e-24 | 37/48 (LoVo, HS-578T, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.276×** | -10.1 | 4e-22 | 41/48 (HT-29, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.523×** | -9.8 | 1e-20 | 34/46 (AsPC-1, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.535×** | -9.4 | 4e-19 | 36/48 (H4, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.526×** | -9.3 | 9e-19 | 31/42 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.520×** | -9.1 | 5e-18 | 22/35 (NCI-H460, HCT15, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.595×** | -7.8 | 3e-13 | 31/48 (HOP62, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **0.583×** | -7.8 | 3e-13 | 24/34 (SW480, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.597×** | -7.8 | 3e-13 | 28/48 (HS-578T, H4, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.616×** | -7.3 | 1e-11 | 32/45 (HOP62, H4, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **0.616×** | -7.2 | 3e-11 | 27/40 (A498, LoVo, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.407×** | -7.1 | 5e-11 | 31/45 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.644×** | -6.6 | 1e-09 | 28/48 (HS-578T, A498, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.668×** | -6.1 | 4e-08 | 32/48 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.676×** | -5.9 | 1e-07 | 23/48 (RPMI-7951, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.767×** | -5.7 | 4e-07 | 23/48 (HS-578T, RPMI-7951, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.711×** | -5.1 | 7e-06 | 25/45 (H4, SW 900, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.697×** | -5.0 | 1e-05 | 24/44 (NCI-H460, H4, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.645×** | -4.7 | 5e-05 | 21/45 (SW1417, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.760×** | -4.0 | 0.001 | 21/47 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -4.0 | 0.001 | 17/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.852× | -3.4 | 0.013 | 10/48 (HOP62, HT-29, …) | all doses, flat |  |
| [[Simotinib (drug)]] 0.05 µM |  | **0.793×** | -3.2 | 0.023 | 16/46 (SW1417, RKO, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.816×** | -3.1 | 0.037 | 12/48 (HT-29, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 39.1 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0901× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.103× (z -13.1) |
| [[HS-578T (line)]] | alt | 32.8 | 0 | 8 (7 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.117× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 17.0 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.205× (z -12.1) |
| [[HOP62 (line)]] | alt | 40.2 | 0 | 7 (6 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.178× (z -12.8) |
| [[A498 (line)]] | wt | 51.8 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.161× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 33.5 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.128× (z -11.6) |
| [[LoVo (line)]] | wt | 45.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[HT-29 (line)]] | alt | 47.2 | 0 | 4 (3 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0575× (z -11.5) |
| [[SW480 (line)]] | alt | 46.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.339× (z -8.9) |
| [[COLO 205 (line)]] | alt | 63.8 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.223× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 58.1 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.184× (z -12.3) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.318× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[NCI-H2030 (line)]] | alt | 22.3 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.208× (z -10.0) ⚠ toxic |
| [[SW48 (line)]] | wt | 19.4 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.112× (z -9.0) ⚠ toxic · without an alert: [[Bendamustine (drug)]] 5 µM 0.114× (z -8.9) |
| [[A549 (line)]] | wt | 19.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.153× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 29.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.264× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[SW 900 (line)]] | alt | 25.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.146× (z -11.2) |
| [[C32 (line)]] | wt | 19.4 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0463× (z -9.0) |
| [[HCT15 (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0951× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -11.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.180× (z -12.1) ⚠ toxic |
| [[LS 180 (line)]] | wt | 40.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[NCI-H1573 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.133× (z -13.8) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.248× (z -8.5) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -10.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[SNU-1 (line)]] | wt | 21.0 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.108× (z -9.8) |
| [[SNU-423 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW1417 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[A-172 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDXDC2P-NPIPB14P]] | +0.81 | +0.76 / +0.88 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PDXDC1]] | +0.75 | +0.70 / +0.83 | both halves | 7e-06 |  |
| [[PDXDC2P]] | +0.71 | +0.64 / +0.81 | both halves | 7e-06 | ⚠ same locus (14.6 kb, same strand: neighbours can correlate without regulation) |
| [[GOLGA2]] | +0.67 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[HYPK]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[PGM3]] | +0.64 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[SLC15A2]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SERP1]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[MCEE]] | +0.62 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[UBE2CP5]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[KDELR2]] | +0.62 | +0.57 / +0.71 | both halves | 8e-06 |  |
| [[SAFB2]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[SLC39A7]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[NDEL1]] | +0.61 | +0.53 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPZOS]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMARCA2]] | B | SMARCA2 activity raises NPIPB14P's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without SMARCA2 | 0.074 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |
| [[TMEM106A]] | B | TMEM106A activity raises NPIPB14P's level | lines that do not express TMEM106A (5) vs lines expressing it (45) | 1.32× lower at baseline in the lines without TMEM106A | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDXDC2P-NPIPB14P]] | C | NPIPB14P's natural level strengthens PDXDC2P-NPIPB14P's drug response | NPIPB14P's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.53; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.8, -35.4); signed map (-49.5, 11.1). **Vector** length 91.5, 23.2% of its response variance represented; |z| ≥ 3 in 1,264 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.6 | -4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | -1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | -3.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.7 | +0.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.7 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -13.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -6.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -10.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.8 | -5.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -7.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | nuclear pore complex interacting protein family member B14, pseudogene |
| Locus type | pseudogene |
| Location | 16q22.1 — chr16:69,976,388-69,996,188 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41990) · Entrez [109729168](https://www.ncbi.nlm.nih.gov/gene/109729168) · Ensembl [ENSG00000226232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226232)

## Data

Gene col 13519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13519); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13519]; `tensor/DDL_lfc|DDL_z.npy` [13519]; `embed/gene_vectors.npy` [13519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13519 or target_col == 13519). Every well: [[NPIPB14P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPIPB14P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
