---
symbol: "AEN"
type: "gene"
col: 11158
ensembl_id: "ENSG00000181026"
name: "apoptosis enhancing nuclease"
location: "15q26.1"
module: 62
arm: "+"
pooled_cpm: 20.55
n_lines_expressing: 49
n_dd_up: 50
n_dd_down: 7
n_dd_up_clean: 35
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# AEN

*apoptosis enhancing nuclease* — 15q26.1

> [!summary] In one line
> AEN, also called ISG20L1, is a p53-inducible nuclear exonuclease that degrades nucleic acid during apoptosis and is needed for efficient DNA fragmentation downstream of p53.

## What it is

AEN (apoptosis-enhancing nuclease) is a small exonuclease of the ISG20/exonuclease-I family, encoded at 15q26.1 and also known as ISG20L1. It carries the conserved exonuclease motifs of that family and has reported activity against single- and double-stranded DNA as well as RNA. In unstressed cells the protein is concentrated in the nucleolus; on induction of apoptosis it redistributes into the nucleoplasm, which is where its substrate is. Mutating the catalytic motifs abolishes both the nuclease activity and the ability to enhance cell death, so the two properties are coupled rather than coincidental.

AEN is a direct transcriptional target of p53 and one of the more reliably recovered members of p53 response signatures across transcriptome studies. Its induction is not p53-exclusive: transcription is driven by all three p53-family members, so p63 and p73 can also raise it. Functionally it has been placed in two adjacent processes. In the first, it is required for efficient internucleosomal DNA fragmentation during p53-dependent apoptosis — loss of AEN reduces fragmentation without necessarily abolishing upstream death signalling, which fits a role as an executioner rather than an initiator. In the second, it modulates genotoxic-stress-induced autophagy, with knockdown reducing autophagic vacuoles and LC3-II after damage. There is no established clinical or therapeutic angle on AEN.

## What is uncertain

Whether the nuclease activity is the function that matters in cells, or whether AEN also acts as a scaffold, has not been separated cleanly — the catalytic-mutant experiments show the activity is required for the death-enhancing phenotype, not that nothing else is going on. The autophagy role comes essentially from one laboratory and has not been broadly replicated. The in vivo requirement is weakly established: AEN is dispensable for most of p53's phenotypic output in the systems where it has been examined, which is consistent with a downstream amplifier rather than a decision point. And because p53-family members share its promoter, induction in a pooled, mixed-genotype screen is not by itself evidence that p53 specifically was active.

## References

- Kawase et al., 2008, Oncogene — identified AEN as a direct p53 target gene encoding a nuclear exonuclease required for efficient DNA fragmentation in p53-dependent apoptosis.
- Eby et al., 2010, Molecular Cancer — showed ISG20L1/AEN is transcriptionally controlled by all three p53-family members and that its loss reduces genotoxic-stress-induced autophagy.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 50 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 7.74× (z +24.6, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.682× (z -4.6, q 0.003, down in 19 of 47 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 0.5 µM: 0.694× (z -4.4, q 0.003, down in 16 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAX]] (+0.63, fdr 1e-05), [[ACTA2]] (+0.61, fdr 1e-05), [[EDA2R]] (+0.60, fdr 2e-05); moves opposite to [[KANTR]] (-0.60, fdr 1e-05), [[SNX3]] (-0.60, fdr 1e-05), [[FXR1]] (-0.55, fdr 1e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); 3 go from it, the strongest it → [[FBXO22]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 50 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11158.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.74×** | +24.6 | 0e+00 | 44/45 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.23×** | +24.6 | 0e+00 | 39/44 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.07×** | +16.2 | 0e+00 | 40/45 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.51×** | +15.1 | 0e+00 | 44/45 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.46×** | +14.9 | 0e+00 | 41/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.23×** | +14.1 | 3e-43 | 37/45 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.77×** | +12.3 | 1e-32 | 43/46 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.63×** | +11.6 | 3e-29 | 41/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.39×** | +10.5 | 7e-24 | 33/46 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.30×** | +9.3 | 1e-18 | 27/32 (LoVo, C32, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.95×** | +8.2 | 9e-15 | 31/46 (A498, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.82×** | +7.2 | 3e-11 | 27/46 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.86×** | +7.2 | 3e-11 | 30/43 (NCI-H460, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.83×** | +7.0 | 1e-10 | 30/43 (RKO, LS 180, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.1 | 3e-08 | 27/47 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +5.3 | 3e-06 | 22/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.34×** | +5.0 | 2e-05 | 20/47 (J82, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.23×** | +4.8 | 4e-05 | 17/42 (hTERT-HPNE, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 2e-04 | 20/46 (SW48, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11158.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.682×** | -4.6 | 0.003 | 19/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.694×** | -4.4 | 0.003 | 16/46 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.697×** | -4.2 | 0.005 | 22/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.509×** | -4.1 | 0.007 | 14/46 (SW480, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.755×** | -3.8 | 0.014 | 19/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.754×** | -3.3 | 0.093 | 17/46 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.765×** | -3.2 | 0.096 | 18/46 (PANC-1, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.756× | -3.1 | 0.13 | 12/45 (HCT15, COLO 205, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.600× | -3.1 | 0.13 | 10/45 (RKO, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.777× | -3.1 | 0.13 | 11/47 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.813× | -3.0 | 0.13 | 14/47 (SK-MEL-2, SW480, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11158. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.8 | 12 (3 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 9.32× (z +16.1) | — |
| [[LoVo (line)]] | wt | 44.8 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +19.9) | — |
| [[A498 (line)]] | wt | 38.9 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 39.3 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.73× (z +14.7) | — |
| [[A549 (line)]] | wt | 75.8 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 11.4× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 25.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 19.3× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 14.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +14.8) | — |
| [[AsPC-1 (line)]] | alt | 8.62 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 26.3× (z +18.1) | [[Selinexor (drug)]] 5 µM 0.186× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 12.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +13.4) | [[Adagrasib (drug)]] 0.05 µM 0.574× (z -10.6) ⚠ position not correctable |
| [[hTERT-HPNE (line)]] | wt | 26.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 11.2× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 30.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.59× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 21.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 7.51× (z +11.6) | [[Adagrasib (drug)]] 0.05 µM 0.654× (z -8.8) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 20.7 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 12.4× (z +11.7) | — |
| [[J82 (line)]] | alt | 15.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +13.1) | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +18.2) | — |
| [[RKO (line)]] | wt | 44.3 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.76× (z +13.6) | — |
| [[SW480 (line)]] | alt | 14.7 | 1 | 2 | [[Digitoxin (drug)]] 0.5 µM 3.35× (z +8.5) | [[Cobimetinib (drug)]] 5 µM 0.238× (z -9.8) |
| [[C32 (line)]] | wt | 28.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.74× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 6.49 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 9.72 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +9.1) | — |
| [[H4 (line)]] | wt | 24.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.21× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 7.68 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +14.6) | — |
| [[NCI-H1792 (line)]] | alt | 6.74 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 18.2× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 19.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +14.2) | — |
| [[SNU-1 (line)]] | wt | 38.3 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 5.68× (z +9.3) | — |
| [[SW48 (line)]] | wt | 34.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.26× (z +11.4) | — |
| [[A-427 (line)]] | wt | 19.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.208× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 28.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 9.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 1 | — | [[Binimetinib (drug)]] 0.5 µM 0.190× (z -9.7) |
| [[SW 900 (line)]] | alt | 6.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11158), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAX]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[ACTA2]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[EDA2R]] | +0.60 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[CDKN1A]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 429 |
| [[XPC]] | +0.59 | +0.53 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[PTCHD4]] | +0.59 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[TEP1]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[TIGAR]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[SPATA18]] | +0.56 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[ZNF195]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[GAS6-AS1]] | +0.55 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[FAS]] | +0.55 | +0.40 / +0.54 | both halves | 5e-05 | pathway: HALLMARK_P53_PATHWAY |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANTR]] | -0.60 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SNX3]] | -0.60 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[FXR1]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ANKMY2]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SUFU]] | -0.51 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[PPP1R2]] | -0.50 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[HSPB11]] | -0.49 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[PRUNE1]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[MACO1]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[RTN3]] | -0.49 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[GLG1]] | -0.48 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[MBOAT2]] | -0.48 | -0.46 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 1, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity raises AEN's level | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | 2.40× lower at baseline in the TP53-altered lines | 0.048 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[PINCR]] | B | PINCR activity raises AEN's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.29× lower at baseline in the lines without PINCR | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[EDA2R]] | B | EDA2R activity raises AEN's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.74× lower at baseline in the lines without EDA2R | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[TOP2A]] | B | TOP2A activity lowers AEN's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.4% of all compounds | 0.015 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens AEN's drug response | lines that do not express PINCR (27) vs lines expressing it (19) | the lines without PINCR respond 0.73× as strongly (z diff +1.58); strongest at Harringtonine 0.5 µM: 2.67x vs 4.33x (z diff +3.0) | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity raises AEN's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.90× lower at baseline in the lines without PTCHD4 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[TP53]] | C | TP53 activity strengthens AEN's drug response | recorded loss-of-function mutation of TP53 in 29 lines vs 17 not recorded | the TP53-altered lines respond 0.73× as strongly (z diff +1.56); strongest at Homoharringtonine 0.05 µM: 1.92x vs 3.35x (z diff +3.0) | 0.699 over the table, 0.043 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; lower baseline (lost expression?); the reference differs; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO22]] | C | AEN's natural level strengthens FBXO22's drug response | AEN's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.54; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ACTA2]] | C | AEN's natural level strengthens ACTA2's drug response | AEN's natural level across 35 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.39; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ASCC3]] | C | AEN's natural level strengthens ASCC3's drug response | AEN's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.59; direction not clear | 0.091 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.2, 37.8); signed map (43.3, -24.1). **Vector** length 96.1, 26.7% of its response variance represented; |z| ≥ 3 in 1,336 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +24.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +6.0 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.4 | +7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +10.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +3.3 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.8 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | +4.8 |

## What is on record

|  |  |
|---|---|
| Name | apoptosis enhancing nuclease |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:88,621,337-88,632,281 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12484, FLJ12562; previously ISG20L1 |
| Gene groups (HGNC) | Exonucleases; MicroRNA protein coding host genes |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WTP8](https://www.uniprot.org/uniprotkb/Q8WTP8) (Apoptosis-enhancing nuclease):

> Exonuclease with activity against single- and double-stranded DNA and RNA. Mediates p53-induced apoptosis. When induced by p53 following DNA damage, digests double-stranded DNA to form single-stranded DNA and amplifies DNA damage signals, leading to enhancement of apoptosis.

**Summary**, from NCBI Gene [64782](https://www.ncbi.nlm.nih.gov/gene/64782):

> Enables DNA exonuclease activity. Involved in intrinsic apoptotic signaling pathway in response to DNA damage by p53 class mediator and response to ionizing radiation. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25722](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25722) · Entrez [64782](https://www.ncbi.nlm.nih.gov/gene/64782) · UniProt [Q8WTP8](https://www.uniprot.org/uniprotkb/Q8WTP8) · Ensembl [ENSG00000181026](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181026)

## Data

Gene col 11158: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11158); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11158, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11158]; `tensor/DDL_lfc|DDL_z.npy` [11158]; `embed/gene_vectors.npy` [11158]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11158 or target_col == 11158). Every well: [[AEN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/AEN.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
