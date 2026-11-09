---
symbol: "MDM2"
type: "gene"
col: 5741
ensembl_id: "ENSG00000135679"
name: "MDM2 proto-oncogene"
location: "12q15"
module: 62
arm: "+"
pooled_cpm: 294.98
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 11
n_dd_up_clean: 18
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 17
direction_downstream: 9
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# MDM2

*MDM2 proto-oncogene* — 12q15

> [!summary] In one line
> MDM2 is the E3 ubiquitin ligase that binds, silences and destroys p53, and is itself one of p53's most strongly induced target genes — the negative feedback loop at the centre of p53 control.

## What it is

MDM2 is a three-part protein. Its N-terminal hydrophobic cleft grips the p53 transactivation domain through three p53 residues — Phe19, Trp23, Leu26 — which blocks coactivator recruitment and switches p53 off as a transcription factor. A central acidic region makes a second, weaker contact with the p53 core and is required for efficient degradation. The C-terminal RING is the catalytic end: MDM2 is a genuine E3 ubiquitin ligase for p53, polyubiquitinating it for proteasomal destruction and, at lower MDM2 levels, monoubiquitinating it in a way that favours nuclear export. p53 protein is consequently short-lived in unstressed cells not because it is made slowly but because MDM2 is constantly removing it.

The mouse genetics are unambiguous: *Mdm2*-null embryos die very early and deleting *Trp53* rescues them completely, so MDM2's essential job is restraining p53.

Regulation is a loop. p53 binds an internal P2 promoter in MDM2's first intron, so activating p53 raises MDM2 transcription, which then lowers p53 — the topology that produces the pulsatile p53 dynamics seen in single cells. The loop is broken from several directions: ATM-dependent phosphorylation of p53 at Ser15 and of MDM2 itself weakens the interaction after DNA damage; p14ARF sequesters MDM2 in the nucleolus; ribosomal proteins bind the acidic domain under ribosomal stress; and [[MDM4]] heterodimerises with MDM2 through the RING and tunes its activity. Clinically, MDM2 is amplified rather than mutated, classically in sarcomas and generally in tumours that retain wild-type TP53. It is the target of the nutlins and their clinical successors, which occupy the p53-binding cleft and so reactivate p53 only where TP53 is intact.

## What is uncertain

MDM2 mRNA is not MDM2 activity. Phosphorylation, ARF sequestration, ribosomal-protein binding and MDM4 partnership all gate the ligase without changing the transcript, so transcript-level inference about the brake's strength is weak. Total MDM2 mRNA also mixes two pools — constitutive P1 output and p53-driven P2 output — and the usual measurement does not separate them, which matters when comparing wild-type against TP53-altered lines, since residual MDM2 expression there is P1, not residual p53. MDM2 has p53-independent substrates and non-catalytic activities that are real but less well mapped; how much of its oncogenic effect is p53-independent remains open. And because the loop oscillates with a period of a few hours in some systems, equal 24 h averages can arise from different pulse behaviour — a limit of the timepoint, not of the gene.

## References

- Momand et al., 1992, Cell — the mdm-2 product forms a complex with p53 and inhibits p53-mediated transactivation.
- Oliner et al., 1992, Nature — identified amplification of the gene encoding this p53-associated protein in human sarcomas.
- Wu et al., 1993, Genes & Development — described the p53–mdm-2 autoregulatory feedback loop.
- Haupt et al., 1997, Nature, and Kubbutat et al., 1997, Nature — showed that Mdm2 promotes rapid p53 degradation and controls p53 stability.
- Honda et al., 1997, FEBS Letters — identified MDM2 as a ubiquitin ligase E3 for p53.
- Vassilev et al., 2004, Science — in vivo activation of the p53 pathway by small-molecule MDM2 antagonists (the nutlins).

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.77× (z +12.2, q 2e-31, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.461× (z -16.6, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TP53I3]] (+0.79, fdr 7e-06), [[FAS]] (+0.77, fdr 7e-06), [[SPATA18]] (+0.77, fdr 1e-05); moves opposite to [[NAA10]] (-0.51, fdr 1e-04, ⚠ NAA10 in the vector space only through flagged drug-doses), [[TNFAIP8L1]] (-0.51, fdr 2e-04), [[FARP2]] (-0.50, fdr 4e-05), [[KIAA1328]] (-0.50, fdr 3e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); 9 go from it, the strongest it → [[FBXO22]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5741.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +12.2 | 2e-31 | 35/48 (RKO, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +11.4 | 1e-27 | 38/48 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +10.5 | 1e-23 | 35/48 (RKO, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +9.9 | 5e-21 | 42/48 (SW48, RKO, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +9.7 | 2e-20 | 31/48 (MIA PaCa-2, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.54×** | +9.2 | 2e-18 | 44/48 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +8.7 | 2e-16 | 34/48 (RKO, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +8.4 | 5e-15 | 41/49 (A498, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +7.6 | 1e-12 | 42/48 (LOX-IMVI, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +7.0 | 2e-10 | 31/49 (SNU-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.37×** | +6.8 | 5e-10 | 29/49 (SW48, SNU-1, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.34×** | +6.3 | 1e-08 | 37/49 (CHP-212, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +6.1 | 6e-08 | 27/38 (SNU-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +6.0 | 7e-08 | 27/48 (SW48, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.22×** | +5.9 | 1e-07 | 24/48 (RKO, SW48, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +5.5 | 1e-06 | 20/48 (RKO, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5741.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.461×** | -16.6 | 0e+00 | 46/48 (HepG2/C3A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.484×** | -15.5 | 0e+00 | 46/48 (HepG2/C3A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.547×** | -12.9 | 9e-36 | 44/48 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.659×** | -8.9 | 6e-17 | 30/48 (LoVo, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.661×** | -8.9 | 9e-17 | 41/48 (HepG2/C3A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -8.6 | 7e-16 | 26/44 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.704×** | -7.5 | 4e-12 | 41/48 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.807×** | -4.4 | 6e-04 | 24/47 (LoVo, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.814×** | -4.4 | 6e-04 | 23/49 (LoVo, A-427, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.676×** | -4.4 | 6e-04 | 27/49 (SW480, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.846× | -3.5 | 0.029 | 15/47 (A549, NCI-H23, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.749×** | -3.2 | 0.058 | 10/46 (RKO, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.903× | -3.1 | 0.089 | 10/48 (AsPC-1, J82, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.905× | -3.0 | 0.094 | 6/48 (A549, A-427, …) | top dose only |  |
| [[Allantoin (drug)]] 5 µM |  | 0.905× | -3.0 | 0.094 | 8/48 (MIA PaCa-2, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5741. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 412 | 20 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 7.49× (z +21.5) | [[Panobinostat (drug)]] 5 µM 0.360× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 577 | 18 (4 ⚠) | 3 | [[Selinexor (drug)]] 5 µM 4.12× (z +16.2) | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -9.8) |
| [[SW48 (line)]] | wt | 346 | 17 (2 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 14.3× (z +20.4) | — |
| [[LoVo (line)]] | wt | 812 | 9 (1 ⚠) | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +16.3) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Selinexor (drug)]] 5 µM 3.31× (z +16.1) | [[Auranofin (drug)]] 5 µM 0.238× (z -13.6) |
| [[SNU-1 (line)]] | wt | 283 | 14 (2 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 9.09× (z +26.9) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.371× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 350 | 14 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 9.40× (z +27.4) | [[Panobinostat (drug)]] 5 µM 0.358× (z -8.9) |
| [[A549 (line)]] | wt | 889 | 9 | 5 (2 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 4.90× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.145× (z -15.5) |
| [[A-427 (line)]] | wt | 520 | 9 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +18.9) | [[Panobinostat (drug)]] 5 µM 0.303× (z -13.3) |
| [[A498 (line)]] | wt | 678 | 9 | 4 (2 ⚠) | [[Selinexor (drug)]] 5 µM 3.02× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.273× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 613 | 5 (1 ⚠) | 6 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.62× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -17.1) |
| [[LS 180 (line)]] | wt | 482 | 9 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 5.12× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 385 | 7 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 7.45× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.212× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 311 | 4 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.379× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 115 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +33.7) | [[Panobinostat (drug)]] 5 µM 0.396× (z -11.4) |
| [[J82 (line)]] | alt | 142 | 7 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +14.6) | — |
| [[NCI-H2347 (line)]] | alt | 423 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +17.4) | [[Panobinostat (drug)]] 5 µM 0.342× (z -11.1) |
| [[C32 (line)]] | wt | 607 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 4.89× (z +9.6) | [[Auranofin (drug)]] 5 µM 0.175× (z -10.5) |
| [[CHP-212 (line)]] | wt | 383 | 4 | 1 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 7.86× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -8.7) |
| [[SW480 (line)]] | alt | 114 | 2 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 1.73× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.68× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.529× (z -11.9) |
| [[A-172 (line)]] | wt | 460 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 6.57× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 172 | 2 | 2 | [[Harringtonine (drug)]] 5 µM 2.55× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.446× (z -9.9) |
| [[C-33 A (line)]] | alt | 152 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 192 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -12.6) |
| [[SW1417 (line)]] | alt | 130 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +24.9) | — |
| [[AN3 CA (line)]] | alt | 165 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.85× (z +10.0) | — |
| [[H4 (line)]] | wt | 442 | 2 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 6.49× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 136 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.505× (z -9.5) |
| [[KATO III (line)]] | alt | 97.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.500× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 99.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.449× (z -8.7) |
| [[PANC-1 (line)]] | alt | 149 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.565× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 106 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.501× (z -8.7) |
| [[BT-474 (line)]] | alt | 219 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +13.9) | — |
| [[CFPAC-1 (line)]] | alt | 181 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.453× (z -8.7) |
| [[COLO 205 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -8.6) |
| [[HCT15 (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.446× (z -9.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 288 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.376× (z -9.1) |
| [[HT-29 (line)]] | alt | 106 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.457× (z -8.9) |
| [[SHP-77 (line)]] | alt | 167 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 116 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +13.0) | — |
| [[SNU-423 (line)]] | alt | 123 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.449× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 492 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 183 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5741), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TP53I3]] | +0.79 | +0.65 / +0.75 | both halves | 7e-06 | STRING 645 |
| [[FAS]] | +0.77 | +0.64 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 428 |
| [[SPATA18]] | +0.77 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[EDA2R]] | +0.76 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[ACTA2]] | +0.76 | +0.58 / +0.76 | both halves | 7e-06 | pathway: Adherens junctions interactions |
| [[ZMAT3]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 520 |
| [[DCP1B]] | +0.74 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[BAX]] | +0.73 | +0.55 / +0.73 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 459 |
| [[PTCHD4]] | +0.73 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[ABCA12]] | +0.73 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[BLOC1S2]] | +0.73 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ZNF79]] | +0.72 | +0.62 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA10]] ⚠ | -0.51 | -0.36 / -0.32 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TNFAIP8L1]] | -0.51 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[FARP2]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 | pathway: Adherens junctions interactions |
| [[KIAA1328]] | -0.50 | -0.29 / -0.35 | both halves | 3e-04 |  |
| [[TPST2]] | -0.50 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[SMYD3]] | -0.49 | -0.34 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 1, B 11, C 5. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity raises MDM2's level | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | 3.02× lower at baseline in the TP53-altered lines | 4e-04 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[PINCR]] | B | PINCR activity raises MDM2's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.44× lower at baseline in the lines without PINCR | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[PTCHD4]] | B | PTCHD4 activity raises MDM2's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 2.31× lower at baseline in the lines without PTCHD4 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[EDA2R]] | B | EDA2R activity raises MDM2's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.84× lower at baseline in the lines without EDA2R | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[PTCHD4]] | B | PTCHD4 activity strengthens MDM2's drug response | lines that do not express PTCHD4 (33) vs lines expressing it (15) | the lines without PTCHD4 respond 0.67× as strongly (z diff +2.43); rises at some drug-doses, falls at others (74% from rises): Idarubicin (hydrochloride) 0.5 µM: 1.54x vs 4.67x (z diff +5.2); Auranofin 5 µM: 0.75x vs 0.40x (z diff +4.6); Selinexor 5 µM: 1.40x vs 2.99x (z diff +3.7) | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[ACTA2]] | B | ACTA2 activity raises MDM2's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.81× lower at baseline in the lines without ACTA2 | 0.051 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[PINCR]] | B | PINCR activity strengthens MDM2's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.65× as strongly (z diff +1.98); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.42x vs 4.19x (z diff +3.9) | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[PURPL]] | B | PURPL activity raises MDM2's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.80× lower at baseline in the lines without PURPL | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[GRIN2C]] | B | GRIN2C activity raises MDM2's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.69× lower at baseline in the lines without GRIN2C | 0.079 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[CYFIP2]] | B | CYFIP2 activity raises MDM2's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 1.77× lower at baseline in the lines without CYFIP2 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[TOP2A]] | B | TOP2A activity lowers MDM2's level | compounds that target TOP2A: 3 of 5 raise it (Amsacrine, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises MDM2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO22]] | C | MDM2's natural level strengthens FBXO22's drug response | MDM2's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.81, reverse +0.55; direction not clear | 5e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[DDB2]] | C | MDM2's natural level strengthens DDB2's drug response | MDM2's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.57; direction not clear | 0.010 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TMEM68]] | C | MDM2's natural level strengthens TMEM68's drug response | MDM2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.34; direction not clear | 0.014 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[FAS]] | C | MDM2's natural level strengthens FAS's drug response | MDM2's natural level across 40 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.24; direction not clear | 0.016 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[TP53INP1]] | C | MDM2's natural level strengthens TP53INP1's drug response | MDM2's natural level across 40 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.50; direction not clear | 0.029 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[ACTA2]] | C | MDM2's natural level strengthens ACTA2's drug response | MDM2's natural level across 36 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.68; direction not clear | 0.037 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[GPX1]] | C | MDM2's natural level strengthens GPX1's drug response | MDM2's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.68, reverse -0.07; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ANKRA2]] | C | MDM2's natural level strengthens ANKRA2's drug response | MDM2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.31; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[BRMS1L]] | C | MDM2's natural level strengthens BRMS1L's drug response | MDM2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.27; direction not clear | 0.068 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.9, 36.2); signed map (42.1, -23.7). **Vector** length 143, 48.2% of its response variance represented; |z| ≥ 3 in 1,678 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.67 to 6); *apoptosis* (hallmark, mean cos +0.62 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +14.2 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +12.2 | +10.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +9.8 | +9.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +9.0 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | +8.7 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.7 | +5.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +7.7 | +5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +6.0 | +5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.8 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.6 | -12.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.0 | -16.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.0 | -15.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.5 | -7.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | -6.2 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -8.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | MDM2 proto-oncogene |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:68,808,177-68,845,544 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HDM2, MGC5370 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers RANBP2-type; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | P53_PATHWAY |
| Reactome | 49 pathways, smallest: AKT phosphorylates targets in the cytosol; SUMOylation of transcription factors; NPAS4 regulates expression of target genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00987](https://www.uniprot.org/uniprotkb/Q00987) (E3 ubiquitin-protein ligase Mdm2):

> E3 ubiquitin-protein ligase that mediates ubiquitination of p53/TP53, leading to its degradation by the proteasome. Inhibits p53/TP53- and p73/TP73-mediated cell cycle arrest and apoptosis by binding its transcriptional activation domain. Also acts as a ubiquitin ligase E3 toward itself and ARRB1. Permits the nuclear export of p53/TP53. Promotes proteasome-dependent ubiquitin-independent degradation of retinoblastoma RB1 protein. Inhibits DAXX-mediated apoptosis by inducing its ubiquitination …

**Summary**, from NCBI Gene [4193](https://www.ncbi.nlm.nih.gov/gene/4193):

> This gene encodes a nuclear-localized E3 ubiquitin ligase. The encoded protein can promote tumor formation by targeting tumor suppressor proteins, such as p53, for proteasomal degradation. This gene is itself transcriptionally-regulated by p53. Overexpression or amplification of this locus is detected in a variety of different cancers. There is a pseudogene for this gene on chromosome 2. Alternative splicing results in a multitude of transcript variants, many of which may be expressed only in …

**Accessions** — [HGNC:6973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6973) · Entrez [4193](https://www.ncbi.nlm.nih.gov/gene/4193) · UniProt [Q00987](https://www.uniprot.org/uniprotkb/Q00987) · Ensembl [ENSG00000135679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135679)

## Data

Gene col 5741: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5741); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5741, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5741]; `tensor/DDL_lfc|DDL_z.npy` [5741]; `embed/gene_vectors.npy` [5741]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5741 or target_col == 5741). Every well: [[MDM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/MDM2.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
