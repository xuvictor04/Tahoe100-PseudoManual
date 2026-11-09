---
symbol: "CDKN1A"
type: "gene"
col: 4563
ensembl_id: "ENSG00000124762"
name: "cyclin dependent kinase inhibitor 1A"
location: "6p21.2"
module: 62
arm: "+"
pooled_cpm: 66.32
n_lines_expressing: 47
n_dd_up: 41
n_dd_down: 6
n_dd_up_clean: 35
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 13
direction_downstream: 10
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# CDKN1A

*cyclin dependent kinase inhibitor 1A* — 6p21.2

> [!summary] In one line
> CDKN1A encodes p21, the cyclin-dependent kinase inhibitor through which p53 converts transcription into a stalled cell cycle, and the most reliable mRNA readout that p53 is active.

## What it is

p21 (p21^WAF1/CIP1^) is a small, largely disordered CDK inhibitor. Its N-terminal domain grips the cyclin groove and the CDK active site, inhibiting cyclin E–CDK2 and cyclin A–CDK2 and, at higher stoichiometry, cyclin D–CDK4/6; at low levels it instead acts as an assembly factor for cyclin D–CDK4, which is why its dose matters as much as its presence. Losing CDK2 activity leaves RB hypophosphorylated and E2F targets off, producing G1/S arrest. A separate C-terminal PIP box binds PCNA and blocks processive replication, giving p21 a direct role at the fork as well as at the kinase.

The gene is the archetypal direct p53 target: two canonical p53 response elements sit roughly 1.3 kb and 2.3 kb upstream, and they were the elements that established what a p53 response element looks like. p21 is also the executor of the repression arm of the p53 program — sustained CDK inhibition keeps the DREAM complex assembled on CDE/CHR promoters, so a large block of cell-cycle genes falls without p53 ever binding them. See [[The p21-DREAM axis]].

Regulation runs in both directions. CDKN1A is induced by many p53-independent inputs — TGF-β/SMAD, BRCA1, Sp1/AP-2, differentiation signals, HDAC inhibitors. The protein is short-lived, degraded by CRL4–CDT2 and SCF–SKP2, and AKT phosphorylation at T145 can move it to the cytoplasm, where it restrains apoptotic signalling instead of the cell cycle. That cytoplasmic activity is the origin of the substantial literature arguing p21 is sometimes oncogenic. Notably, CDKN1A is almost never mutated in human cancer; the pathway is bypassed upstream rather than at p21.

## What is uncertain

p21 mRNA reports p53 transcriptional activity, not outcome. Arrest, senescence, apoptosis resistance, or nothing follows depending on context, and the induction alone cannot distinguish them. Because the p53-independent inputs are real and strong, p21 up is necessary but not sufficient evidence that p53 is on — residual induction in a TP53-altered line more likely reflects those other inputs than residual p53. The cytoplasmic anti-apoptotic role means more p21 is not monotonically more tumour suppression. And p21 expression is pulsatile and bimodal at single-cell resolution; a pooled 24 h average smooths over pulse structure that is part of how the signal actually works.

## References

- el-Deiry et al., 1993, Cell — identified WAF1/CDKN1A as a p53-inducible gene and candidate mediator of p53 growth suppression.
- Harper et al., 1993, Cell — characterised p21/Cip1 as a potent inhibitor of G1 cyclin-dependent kinases.
- Waldman, Kinzler & Vogelstein, 1995, Cancer Research — showed p21 is required for p53-mediated G1 arrest in human cancer cells.
- Brugarolas et al., 1995, Nature — radiation-induced cell-cycle arrest is compromised in p21-deficient cells.
- Abbas & Dutta, 2009, Nature Reviews Cancer — review of p21's multiple, partly opposing activities in cancer.
- Engeland, 2018, Cell Death & Differentiation — set out the p53–p21–DREAM route for indirect transcriptional repression.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.92× (z +13.6, q 1e-39, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.687× (z -5.6, q 2e-05, down in 24 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACER2]] (+0.64, fdr 1e-05), [[NTN1]] (+0.62, fdr 1e-05), [[IER5]] (+0.61, fdr 1e-05); moves opposite to [[MPHOSPH9]] (-0.53, fdr 1e-05), [[SHMT1]] (-0.52, fdr 3e-05), [[PARPBP]] (-0.52, fdr 1e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); 10 go from it, the strongest it → [[MAST4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4563.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +13.6 | 1e-39 | 34/45 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.15×** | +11.2 | 7e-27 | 31/45 (KATO III, Panc 03.27, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +10.7 | 2e-24 | 30/44 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +9.5 | 4e-19 | 36/45 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.80×** | +8.7 | 4e-16 | 33/45 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.77×** | +8.4 | 4e-15 | 28/45 (A498, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +7.6 | 2e-12 | 28/45 (PANC-1, HT-29, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +6.9 | 4e-10 | 32/46 (HT-29, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.5 | 6e-09 | 27/45 (A549, A498, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +5.9 | 2e-07 | 26/45 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.5 | 2e-06 | 27/44 (NCI-H1573, SNU-423, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +5.2 | 1e-05 | 23/45 (HS-578T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.43×** | +5.1 | 2e-05 | 23/44 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 3e-05 | 22/46 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 3e-05 | 23/45 (NCI-H2030, Hs 766T, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 3e-05 | 24/44 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.92×** | +4.9 | 3e-05 | 27/44 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4563.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.687×** | -5.6 | 2e-05 | 24/45 (HT-29, AsPC-1, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.503×** | -5.2 | 7e-05 | 23/44 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.727×** | -4.7 | 5e-04 | 24/45 (A549, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.806×** | -4.5 | 9e-04 | 24/45 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.745×** | -4.4 | 0.001 | 22/45 (SNU-423, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.838× | -3.7 | 0.021 | 21/46 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.779×** | -3.6 | 0.031 | 17/45 (HepG2/C3A, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.815× | -3.0 | 0.16 | 12/44 (A498, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 64.0 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +14.9) | — |
| [[A549 (line)]] | wt | 90.2 | 8 (3 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 4.64× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.235× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 211 | 5 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.08× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 90.0 | 0 | 7 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.316× (z -11.5) |
| [[SW48 (line)]] | wt | 173 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 10.6× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[LS 180 (line)]] | wt | 192 | 2 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 4.63× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.191× (z -12.4) |
| [[A-427 (line)]] | wt | 46.0 | 4 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.81× (z +10.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.52× (z +10.3) | — |
| [[KATO III (line)]] | alt | 29.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +18.0) | — |
| [[LoVo (line)]] | wt | 102 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.5) | [[Belumosudil (drug)]] 5 µM 0.284× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 77.3 | 1 (1 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.19× (z +9.0) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.110× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.305× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 80.1 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 4.36× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 73.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +19.3) | — |
| [[HS-578T (line)]] | alt | 45.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +18.0) | — |
| [[LOX-IMVI (line)]] | wt | 124 | 3 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.52× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.38× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 60.7 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.57× (z +11.5) | — |
| [[RKO (line)]] | wt | 57.6 | 2 (1 ⚠) | 1 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.48× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 29.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +14.8) | — |
| [[A-172 (line)]] | wt | 183 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 4.97× (z +11.8) | — |
| [[C32 (line)]] | wt | 121 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +10.9) | — |
| [[H4 (line)]] | wt | 150 | 2 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 3.79× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 17.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +10.3) | — |
| [[HepG2_C3A (line)]] | wt | 89.8 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.60× (z +9.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.08× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 53.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +15.6) | — |
| [[HT-29 (line)]] | alt | 55.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.96× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 67.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.97× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.189× (z -9.5) |
| [[SNU-1 (line)]] | wt | 24.8 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 15.6× (z +9.8) ⚠ toxic | — |
| [[SW 900 (line)]] | alt | 30.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +11.6) | — |
| [[CHP-212 (line)]] | wt | 87.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 7.54× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0916× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 42.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +14.1) | — |
| [[NCI-H2347 (line)]] | alt | 87.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.38× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 35.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.42× (z +9.3) | — |
| [[SW 1271 (line)]] | alt | 72.8 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.109× (z -8.5) |
| [[SW1417 (line)]] | alt | 29.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +12.6) | — |
| [[SW480 (line)]] | alt | 18.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.89× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACER2]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[NTN1]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[IER5]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[GDF15]] | +0.59 | +0.47 / +0.64 | both halves | 2e-05 | STRING 556 |
| [[AEN]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 429 |
| [[CDIP1]] | +0.59 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[GAS6-AS1]] | +0.59 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[NBEAP1]] | +0.59 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[GADD45A]] | +0.59 | +0.47 / +0.57 | both halves | 2e-05 | pathway: HALLMARK_APOPTOSIS; STRING 974 |
| [[BTG2]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS; STRING 621 |
| [[ADAMTS7]] | +0.58 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[MAST4]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH9]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[SHMT1]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[PARPBP]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[NCAPD3]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SKP2]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 | pathway: Aberrant regulation of mitotic cell cycle due to RB1 defects; STRING 996 |
| [[TUBGCP3]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 | pathway: G2/M Transition |
| [[PPIH]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[RAD54B]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[PBK]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[CDK5RAP2]] | -0.47 | -0.44 / -0.46 | both halves | 3e-05 | pathway: G2/M Transition |
| [[IPO11]] | -0.47 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[ERLIN1]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 1, B 10, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity strengthens CDKN1A's drug response | recorded loss-of-function mutation of TP53 in 29 lines vs 17 not recorded | the TP53-altered lines respond 0.85× as strongly (z diff +0.48); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.40x vs 4.04x (z diff +5.9) | 0.019 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; lower baseline (lost expression?); both ways; artifact flags |
| [[C21orf91]] | B | C21orf91 activity raises CDKN1A's level | lines that do not express C21orf91 (5) vs lines expressing it (45) | 3.02× lower at baseline in the lines without C21orf91 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[PHLDA2]] | B | PHLDA2 activity raises CDKN1A's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.55× lower at baseline in the lines without PHLDA2 | 0.009 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[PINCR]] | B | PINCR activity strengthens CDKN1A's drug response | lines that do not express PINCR (26) vs lines expressing it (20) | the lines without PINCR respond 0.92× as strongly (z diff +0.37); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.41x vs 3.60x (z diff +5.1) | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; artifact flags |
| [[ABL1]] | B | ABL1 activity raises CDKN1A's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers CDKN1A's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DUSP5-DT]] | B | DUSP5-DT activity raises CDKN1A's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without DUSP5-DT | 0.055 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent |
| [[LINC01322]] | B | LINC01322 activity raises CDKN1A's level | lines that do not express LINC01322 (35) vs lines expressing it (15) | 1.65× lower at baseline in the lines without LINC01322 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, TM4SF4, TIMD4 |
| [[PINCR]] | B | PINCR activity raises CDKN1A's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.00× lower at baseline in the lines without PINCR | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[EDA2R]] | B | EDA2R activity raises CDKN1A's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.68× lower at baseline in the lines without EDA2R | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[PTCHD4]] | B | PTCHD4 activity strengthens CDKN1A's drug response | lines that do not express PTCHD4 (30) vs lines expressing it (16) | the lines without PTCHD4 respond 1.06× as strongly (z diff +0.15); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.58x vs 3.64x (z diff +5.0) | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; target measured in part of the lines; both ways; artifact flags |
| [[PMAIP1]] | C | PMAIP1 activity raises CDKN1A's level | lines that do not express PMAIP1 (4) vs lines expressing it (46) | 3.78× lower at baseline in the lines without PMAIP1 | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAST4]] | C | CDKN1A activity raises MAST4's level | lines that do not express CDKN1A (3) vs lines expressing it (47) | 5.67× lower at baseline in the lines without CDKN1A | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, FAT1, SFXN3; maybe low, not absent |
| cells under [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM | C | CDKN1A activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express CDKN1A (3) vs lines expressing it (45) | the lines without CDKN1A: 0.74× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, FAT1, SFXN3; maybe low, not absent |
| cells under [[Methylprednisolone succinate (drug)]] 0.5 µM | C | CDKN1A activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express CDKN1A (3) vs lines expressing it (45) | the lines without CDKN1A: 1.52× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, FAT1, SFXN3; maybe low, not absent |
| cells under [[Cyclosporin A (drug)]] 0.05 µM | C | CDKN1A activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express CDKN1A (3) vs lines expressing it (45) | the lines without CDKN1A: 0.69× the cells of the other lines | 0.063 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, FAT1, SFXN3; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 0.5 µM | C | CDKN1A activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express CDKN1A (3) vs lines expressing it (45) | the lines without CDKN1A: 0.21× the cells of the other lines | 0.065 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, FAT1, SFXN3; maybe low, not absent |
| cells under [[Artemether (drug)]] 0.05 µM | C | CDKN1A activity raises the cells' numbers under Artemether 0.05 µM (protects the cells) | lines that do not express CDKN1A (3) vs lines expressing it (45) | the lines without CDKN1A: 0.70× the cells of the other lines | 0.074 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, FAT1, SFXN3; maybe low, not absent |
| [[PHLDA2]] | C | CDKN1A activity raises PHLDA2's level | lines that do not express CDKN1A (3) vs lines expressing it (47) | 3.96× lower at baseline in the lines without CDKN1A | 0.076 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, FAT1, SFXN3; maybe low, not absent |
| cells under [[GSK1059615 (drug)]] 5 µM | C | CDKN1A activity raises the cells' numbers under GSK1059615 5 µM (protects the cells) | lines that do not express CDKN1A (3) vs lines expressing it (45) | the lines without CDKN1A: 0.31× the cells of the other lines | 0.076 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, FAT1, SFXN3; maybe low, not absent |
| [[PMAIP1]] | C | CDKN1A activity raises PMAIP1's level | lines that do not express CDKN1A (3) vs lines expressing it (47) | 3.56× lower at baseline in the lines without CDKN1A | 0.094 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, FAT1, SFXN3; maybe low, not absent |
| [[LACC1]] | C | CDKN1A activity raises LACC1's level | lines that do not express CDKN1A (3) vs lines expressing it (47) | 3.15× lower at baseline in the lines without CDKN1A | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, FAT1, SFXN3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.4, 38.3); signed map (44.2, -22.3). **Vector** length 139, 44.2% of its response variance represented; |z| ≥ 3 in 1,631 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +9.7 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.4 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.1 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.7 | +10.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +6.0 | +4.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +6.0 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +11.2 |
| fall | [[NG25 (drug)]] 5 µM |  | -6.0 | -5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.6 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -1.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -3.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase inhibitor 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:36,676,460-36,687,337 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P21, CIP1, WAF1, SDI1, CAP20, p21CIP1, p21Cip1/Waf1, p21; previously CDKN1 |
| Gene groups (HGNC) | Cyclin dependent kinase inhibitor 1 family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, INFLAMMATORY_RESPONSE, MYOGENESIS, APOPTOSIS, INTERFERON_GAMMA_RESPONSE, HYPOXIA, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY, MTORC1_SIGNALING, E2F_TARGETS |
| Reactome | 65 pathways, smallest: Transcriptional  activation of  cell cycle inhibitor p21; Transcriptional activation of p53 responsive genes; TFAP2 (AP-2) family regulates transcription of cell cycle factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P38936](https://www.uniprot.org/uniprotkb/P38936) (Cyclin-dependent kinase inhibitor 1):

> Plays an important role in controlling cell cycle progression and DNA damage-induced G2 arrest. Involved in p53/TP53 mediated inhibition of cellular proliferation in response to DNA damage. Also involved in p53-independent DNA damage-induced G2 arrest mediated by CREB3L1 in astrocytes and osteoblasts (By similarity). Binds to and inhibits cyclin-dependent kinase activity, preventing phosphorylation of critical cyclin-dependent kinase substrates and blocking cell cycle progression. Functions in …

**Summary**, from NCBI Gene [1026](https://www.ncbi.nlm.nih.gov/gene/1026):

> This gene encodes a potent cyclin-dependent kinase inhibitor. The encoded protein binds to and inhibits the activity of cyclin-cyclin-dependent kinase2 or -cyclin-dependent kinase4 complexes, and thus functions as a regulator of cell cycle progression at G1. The expression of this gene is tightly controlled by the tumor suppressor protein p53, through which this protein mediates the p53-dependent cell cycle G1 phase arrest in response to a variety of stress stimuli. This protein can interact …

**Accessions** — [HGNC:1784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1784) · Entrez [1026](https://www.ncbi.nlm.nih.gov/gene/1026) · UniProt [P38936](https://www.uniprot.org/uniprotkb/P38936) · Ensembl [ENSG00000124762](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124762)

## Data

Gene col 4563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4563); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4563]; `tensor/DDL_lfc|DDL_z.npy` [4563]; `embed/gene_vectors.npy` [4563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4563 or target_col == 4563). Every well: [[CDKN1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/CDKN1A.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
