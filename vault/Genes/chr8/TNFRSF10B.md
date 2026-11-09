---
symbol: "TNFRSF10B"
type: "gene"
col: 4232
ensembl_id: "ENSG00000120889"
name: "TNF receptor superfamily member 10b"
location: "8p21.3"
module: 63
arm: "+"
pooled_cpm: 211.56
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 20
n_dd_up_clean: 17
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/063", "written"]
generated_by: "tahoemap"
---

# TNFRSF10B

*TNF receptor superfamily member 10b* — 8p21.3

> [!summary] In one line
> TNFRSF10B encodes DR5, the principal death receptor for TRAIL and a direct p53 target, through which p53 can route killing through the cell surface rather than the mitochondrion.

## What it is

DR5 (also TRAIL-R2, KILLER, TRICK2) is a type I transmembrane protein of the TNF receptor superfamily. Its cysteine-rich ectodomain binds trimeric TRAIL (TNFSF10); its cytoplasmic death domain then recruits FADD, which brings in caspase-8 and caspase-10 to form the death-inducing signalling complex. Caspase-8 activated there cleaves caspase-3 and -7 directly in so-called type I cells, or cleaves BID and so recruits the mitochondrion in type II cells — meaning the extrinsic pathway usually converges on the same machinery as the intrinsic one. Several layers sit between receptor and death: the decoy receptors TNFRSF10C and TNFRSF10D and soluble osteoprotegerin compete for ligand, cFLIP blocks caspase-8 at the complex, and receptor clustering rather than mere abundance is what licenses signalling. Two splice isoforms differ by a short insertion in the extracellular stalk.

The gene entered the p53 field directly: it was cloned as a DNA-damage-inducible, p53-regulated death receptor, and it appears in essentially every census of p53 targets. It is not only a p53 gene, though. DR5 is a major node of the unfolded protein response, where PERK–CHOP drives its transcription while IRE1α degrades its mRNA through regulated IRE1-dependent decay — the two arms opposing each other on one gene, which turns DR5 into a timer that converts sustained ER stress into ligand-independent apoptosis. NF-κB signalling also raises it. Therapeutically, DR5 was one of oncology's most-attempted targets: recombinant TRAIL and first-generation agonist antibodies were tested widely and largely failed as single agents, which is itself informative about how much of the pathway lies downstream of the receptor.

## What is uncertain

The gap between DR5 mRNA and apoptosis is wide and well documented — most cancer lines carry plenty of DR5 and remain TRAIL-resistant, because cFLIP, decoy receptors, caspase-8 silencing and the absence of ligand all intervene. The bigger caution here is specificity: ER stress induces DR5 strongly and entirely without p53, and in a 379-compound panel many agents stress the endoplasmic reticulum, so DR5 induction is a weaker p53-specific signal than its p53-target status suggests. Its p53 response element is accepted as functional, but DR5 is a multiply-regulated gene rather than a dedicated p53 readout, and the relative weight of p53, CHOP and NF-κB input in any given condition is not something a transcript level can resolve.

## References

- Wu et al., 1997, Nature Genetics — identified KILLER/DR5 as a DNA damage-inducible, p53-regulated death receptor gene.
- Sheridan et al., 1997, Science — placed TRAIL-induced apoptosis under the control of a family of signalling and decoy receptors.
- Lu et al., 2014, Science — showed opposing unfolded-protein-response signals converge on DR5 to set the timing of ER-stress apoptosis.
- Fischer, 2017, Oncogene — census of p53 target genes, in which TNFRSF10B scores as a high-confidence direct target.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.26× (z +18.2, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.461× (z -11.8, q 4e-29, down in 43 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 0.698× (z -5.4, q 1e-05, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDF15]] (+0.65, fdr 1e-05), [[DDIT3]] (+0.61, fdr 7e-06), [[PLK3]] (+0.58, fdr 1e-05); moves opposite to [[ANKRD52]] (-0.44, fdr 7e-05), [[ZC3H14]] (-0.44, fdr 1e-04), [[NCBP3]] (-0.43, fdr 6e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FOSL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4232.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +18.2 | 0e+00 | 41/47 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **8.47×** | +17.6 | 0e+00 | 48/48 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.00×** | +9.0 | 3e-17 | 41/47 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **1.40×** | +7.5 | 1e-11 | 37/47 (SNU-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.3 | 3e-11 | 29/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +6.3 | 3e-08 | 32/47 (RPMI-7951, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.48×** | +6.2 | 5e-08 | 36/46 (SNU-1, SW480, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.40×** | +5.3 | 9e-06 | 31/47 (C-33 A, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 1e-04 | 27/47 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 6e-04 | 29/47 (SW48, SNU-1, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.20× | +4.1 | 0.003 | 21/47 (PANC-1, Hs 766T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.008 | 24/47 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.18× | +3.7 | 0.009 | 20/47 (NCI-H460, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.032 | 23/47 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.035 | 24/47 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.035 | 24/47 (AsPC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4232.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.461×** | -11.8 | 4e-29 | 43/43 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.578×** | -8.6 | 1e-15 | 35/48 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.698×** | -5.4 | 1e-05 | 36/47 (NCI-H1573, SW 900, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.752×** | -5.2 | 3e-05 | 36/47 (HOP62, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.558×** | -4.8 | 2e-04 | 34/46 (Panc 03.27, AN3 CA, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.749×** | -4.6 | 5e-04 | 27/48 (NCI-H1573, SW 900, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.750×** | -4.4 | 0.001 | 29/46 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.785×** | -3.8 | 0.010 | 26/46 (SNU-423, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.842× | -3.8 | 0.011 | 20/47 (NCI-H1573, SNU-423, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.775×** | -3.7 | 0.011 | 23/44 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.803×** | -3.5 | 0.028 | 25/47 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.792×** | -3.4 | 0.029 | 23/47 (NCI-H1573, SW 900, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.812×** | -3.4 | 0.029 | 20/49 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.807×** | -3.4 | 0.029 | 22/47 (MIA PaCa-2, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.816×** | -3.3 | 0.029 | 20/48 (NCI-H1792, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.862× | -3.3 | 0.029 | 13/47 (KATO III, SW1417, …) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.811×** | -3.3 | 0.029 | 19/48 (LS 180, A-172, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.811×** | -3.3 | 0.029 | 21/48 (SNU-423, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 243 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +22.4) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -12.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 252 | 8 | 0 | [[Artesunate (drug)]] 5 µM 2.90× (z +12.4) | — |
| [[HEC-1-A (line)]] | alt | 363 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -17.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 304 | 5 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -11.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 153 | 6 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +14.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.52× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -11.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 379 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 209 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.18× (z +11.4) | [[Ixazomib citrate (drug)]] 5 µM 0.411× (z -9.9) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.572× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 188 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +14.9) | — |
| [[A-172 (line)]] | wt | 301 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -8.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 203 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -11.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 174 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +16.0) | — |
| [[LS 180 (line)]] | wt | 426 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.9× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.153× (z -14.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 182 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.454× (z -9.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 203 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +24.7) | — |
| [[hTERT-HPNE (line)]] | wt | 131 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +15.2) | — |
| [[KATO III (line)]] | alt | 306 | 1 | 3 (3 ⚠) | [[Artesunate (drug)]] 5 µM 2.07× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -15.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 131 | 2 | 2 (1 ⚠) | [[Pentamidine (isethionate) (drug)]] 5 µM 1.89× (z +9.6) | [[Harringtonine (drug)]] 0.5 µM 0.348× (z -11.2) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.390× (z -10.0) |
| [[RKO (line)]] | wt | 280 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +17.5) | — |
| [[RPMI-7951 (line)]] | alt | 126 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 105 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +15.0) | — |
| [[SW48 (line)]] | wt | 322 | 3 | 1 (1 ⚠) | [[Artesunate (drug)]] 5 µM 2.70× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -10.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 87.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +17.2) | — |
| [[CFPAC-1 (line)]] | alt | 198 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -11.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 249 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 154 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +18.9) | — |
| [[HT-29 (line)]] | alt | 358 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -10.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 83.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +21.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 292 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 116 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -12.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 226 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -15.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 304 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 306 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 155 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 126 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.2× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 77.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -18.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 218 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.5) | — |
| [[C-33 A (line)]] | alt | 109 | 1 | 0 | [[5-Azacytidine (drug)]] 5 µM 5.19× (z +14.3) | — |
| [[C32 (line)]] | wt | 61.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +13.8) | — |
| [[H4 (line)]] | wt | 286 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 287 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -9.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 127 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.05× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 137 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 361 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4232), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDF15]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[DDIT3]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 | STRING 727 |
| [[PLK3]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ERN1]] | +0.56 | +0.46 / +0.58 | both halves | 2e-05 | STRING 547 |
| [[SESN2]] | +0.55 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[DLGAP1-AS2]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SYT5]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[LSR]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ERICH2]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[ADM2]] | +0.52 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[RGS16]] | +0.51 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[GOT1]] | +0.51 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD52]] | -0.44 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[ZC3H14]] | -0.44 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[NCBP3]] | -0.43 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[GFM1]] | -0.43 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[VPS45]] | -0.42 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[UBE2K]] | -0.41 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[RBMS1]] | -0.41 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[ELAC2]] | -0.41 | -0.36 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOSL1]] | B | FOSL1 activity raises TNFRSF10B's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 2.35× lower at baseline in the lines without FOSL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[IL1A]] | B | IL1A activity raises TNFRSF10B's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.22× lower at baseline in the lines without IL1A | 0.060 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[MAP2K1]] | B | MAP2K1 activity raises TNFRSF10B's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[PLCH2]] | B | PLCH2 activity weakens TNFRSF10B's drug response | lines that do not express PLCH2 (26) vs lines expressing it (22) | the lines without PLCH2 respond 1.00× as strongly (z diff -0.40); strongest at Idarubicin (hydrochloride) 5 µM: 1.67x vs 1.20x (z diff -3.3) | 0.076 | ⚠ within organs, on part of the lines; also absent: SERPINA5, LINC01814, ACOXL; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.418). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.5, -8.1); signed map (-2.3, 29.1). **Vector** length 136, 48.9% of its response variance represented; |z| ≥ 3 in 1,575 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +8.5 | +7.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +17.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +7.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +5.1 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +3.3 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +4.2 | +3.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +3.5 | +6.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.4 | +3.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.5 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.0 | +3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | +1.7 |
|  | [[NG25 (drug)]] 5 µM |  | -5.2 | -4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.9 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.8 | -3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.8 | -4.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.6 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 10b |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:23,020,133-23,069,031 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DR5, KILLER, TRICK2A, TRAIL-R2, TRICKB, CD262, TRAILR2 |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor receptor superfamily |
| Reactome | 17 pathways, smallest: TRAIL  signaling; CASP8 activity is inhibited; Dimerization of procaspase-8 |
| Matched by | ensembl_id |

**Function**, from UniProt [O14763](https://www.uniprot.org/uniprotkb/O14763) (Tumor necrosis factor receptor superfamily member 10B):

> Receptor for the cytotoxic ligand TNFSF10/TRAIL. The adapter molecule FADD recruits caspase-8 to the activated receptor. The resulting death-inducing signaling complex (DISC) performs caspase-8 proteolytic activation which initiates the subsequent cascade of caspases (aspartate-specific cysteine proteases) mediating apoptosis. Promotes the activation of NF-kappa-B. Essential for ER stress-induced apoptosis.

**Summary**, from NCBI Gene [8795](https://www.ncbi.nlm.nih.gov/gene/8795):

> The protein encoded by this gene is a member of the TNF-receptor superfamily, and contains an intracellular death domain. This receptor can be activated by tumor necrosis factor-related apoptosis inducing ligand (TNFSF10/TRAIL/APO-2L), and transduces an apoptosis signal. Studies with FADD-deficient mice suggested that FADD, a death domain containing adaptor protein, is required for the apoptosis mediated by this protein. Two transcript variants encoding different isoforms and one non-coding …

**Accessions** — [HGNC:11905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11905) · Entrez [8795](https://www.ncbi.nlm.nih.gov/gene/8795) · UniProt [O14763](https://www.uniprot.org/uniprotkb/O14763) · Ensembl [ENSG00000120889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120889)

## Data

Gene col 4232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4232); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4232, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4232]; `tensor/DDL_lfc|DDL_z.npy` [4232]; `embed/gene_vectors.npy` [4232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4232 or target_col == 4232). Every well: [[TNFRSF10B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/TNFRSF10B.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
