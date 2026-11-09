---
symbol: "POLH"
type: "gene"
col: 9997
ensembl_id: "ENSG00000170734"
name: "DNA polymerase eta"
location: "6p21.1"
module: 62
arm: "+"
pooled_cpm: 60.57
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 9
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 10
direction_downstream: 1
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# POLH

*DNA polymerase eta* — 6p21.1

> [!summary] In one line
> POLH encodes DNA polymerase eta, the translesion polymerase that copies accurately past UV photoproducts, and whose loss causes the variant form of xeroderma pigmentosum.

## What it is

Pol eta is a Y-family DNA polymerase — one of the specialists, with pol iota, pol kappa and REV1, that replicate templates the replicative polymerases cannot accommodate. Its signature substrate is the cyclobutane pyrimidine dimer, the commonest UV photoproduct. Where pol delta stalls, pol eta's unusually open and solvent-exposed active site takes the covalently joined dimer in as though it were an ordinary base pair, holding the distorted template in a near-B-form geometry — the "molecular splint" description — and inserting the correct two adenines. The bypass is therefore largely error-free, which makes pol eta a repair-adjacent enzyme rather than simply a mutator.

On undamaged DNA the same open site makes it inaccurate and barely processive, so access is restricted. After a fork stalls, RAD6–RAD18 mono-ubiquitinates PCNA at K164; pol eta reads that mark through its PIP box and UBZ zinc finger. It synthesises a short patch and is displaced — a polymerase switch, not a replacement replicase. Translesion capacity is set mostly by that access machinery.

Biallelic loss of POLH causes xeroderma pigmentosum variant: sun sensitivity and high skin cancer incidence, but with *normal* nucleotide excision repair — the defect is in post-replication damage tolerance, which distinguishes it from the classical XP groups ([[XPC]], [[DDB2]]). Pol eta has a second job in adaptive immunity, generating the A:T mutations of immunoglobulin somatic hypermutation. It also bypasses cisplatin crosslinks, the basis for its association with platinum resistance. POLH is reported as a p53 target: induced by DNA damage p53-dependently, with a p53-binding site identified at its promoter, and its knockdown impairing p53 activation — placing it, like [[PLK3]], among p53 outputs that also feed back on p53.

## What is uncertain

The p53-target status is the soft point. The evidence is coherent but not broadly replicated, the promoter element is not one of the canonical p53 response elements, and POLH is damage-inducible by several routes — so the direct-versus-indirect question is open. The claim that pol eta is required for full p53 activation after damage has not been independently established. A more general caution: translesion synthesis is governed principally by PCNA ubiquitination and regulated access to the stalled fork, so a change in POLH mRNA need not correspond to a change in bypass activity. Finally, pol eta's role in chemoresistance is contested: higher pol eta has been associated with platinum resistance in some settings, while loss of translesion capacity sensitises cells to crosslinkers in others.

## References

- Johnson et al., 1999, Science — mutations in hRAD30/POLH underlie the variant form of xeroderma pigmentosum.
- Masutani et al., 1999, Nature — the XPV gene product is human DNA polymerase eta.
- Zeng et al., 2001, Nature Immunology — pol eta acts as an A:T mutator during somatic hypermutation of immunoglobulin variable genes.
- Liu and Chen, 2006, Molecular and Cellular Biology — POLH is a p53 target whose loss modulates the DNA damage checkpoint and p53 activation.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +17.3, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.582× (z -9.0, q 2e-16, down in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.674× (z -6.7, q 4e-09, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDB2]] (+0.76, fdr 7e-06), [[PPM1D]] (+0.73, fdr 7e-06), [[PHPT1]] (+0.72, fdr 7e-06); moves opposite to [[NUDC]] (-0.62, fdr 1e-05), [[ELAC2]] (-0.61, fdr 1e-05), [[CCT2]] (-0.59, fdr 1e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ACTA2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[EED]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9997.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +17.3 | 0e+00 | 46/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +16.9 | 0e+00 | 38/47 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.50×** | +16.4 | 0e+00 | 46/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.42×** | +15.8 | 0e+00 | 42/47 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.34×** | +15.2 | 0e+00 | 43/47 (SW480, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +12.5 | 7e-34 | 43/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +11.9 | 1e-30 | 38/46 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.80×** | +10.1 | 4e-22 | 41/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.74×** | +9.9 | 4e-21 | 37/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.60×** | +8.4 | 2e-15 | 39/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +8.2 | 1e-14 | 30/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +7.6 | 2e-12 | 35/47 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.41×** | +6.1 | 4e-08 | 32/47 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.6 | 9e-07 | 25/47 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.2 | 8e-06 | 25/47 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.74×** | +5.2 | 9e-06 | 29/47 (PANC-1, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +4.7 | 8e-05 | 26/48 (J82, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.17× | +3.9 | 0.002 | 18/47 (RKO, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.003 | 21/47 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.011 | 15/47 (SNU-423, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.3 | 0.020 | 14/47 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.026 | 8/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.028 | 18/47 (A-427, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9997.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.582×** | -9.0 | 2e-16 | 34/44 (A-427, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -7.3 | 6e-11 | 28/40 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.674×** | -6.7 | 4e-09 | 29/47 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.693×** | -6.6 | 7e-09 | 29/47 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.548×** | -5.6 | 2e-06 | 32/44 (A498, H4, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.754×** | -5.1 | 4e-05 | 29/47 (A-172, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.692×** | -4.9 | 1e-04 | 30/48 (HCT15, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.766×** | -4.6 | 3e-04 | 22/46 (AN3 CA, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.772×** | -4.5 | 5e-04 | 26/47 (LoVo, LS 180, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -3.2 | 0.071 | 0/48 | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.839× | -3.2 | 0.079 | 17/47 (SW 1088, A549, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9997. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 49.0 | 10 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +17.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.9) | — |
| [[A498 (line)]] | wt | 78.1 | 9 (4 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +12.0) | — |
| [[LoVo (line)]] | wt | 81.9 | 7 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.375× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 97.0 | 6 (2 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +14.7) | [[Auranofin (drug)]] 5 µM 0.377× (z -10.5) |
| [[PANC-1 (line)]] | alt | 63.0 | 9 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +16.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.33× (z +16.2) | — |
| [[LS 180 (line)]] | wt | 91.3 | 5 (2 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.0361× (z -28.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 50.6 | 8 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.56× (z +13.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 54.0 | 8 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.11× (z +22.2) | — |
| [[RKO (line)]] | wt | 63.2 | 8 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +16.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 57.7 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +15.2) | — |
| [[A549 (line)]] | wt | 64.3 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +12.7) | — |
| [[HepG2_C3A (line)]] | wt | 68.3 | 6 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.99× (z +13.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 61.0 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.21× (z +13.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 17.1 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 62.4 | 4 (4 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.26× (z +10.0) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -11.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 54.1 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +29.9) | — |
| [[J82 (line)]] | alt | 55.3 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +17.6) | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 30.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +14.6) | — |
| [[SNU-423 (line)]] | alt | 60.8 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +25.7) | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 49.9 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +11.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.3) | — |
| [[A-172 (line)]] | wt | 107 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -11.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 97.1 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 2.91× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0805× (z -25.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.270× (z -14.5) |
| [[Hs 766T (line)]] | wt | 36.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.4) | — |
| [[HS-578T (line)]] | alt | 63.6 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.16× (z +14.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 53.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.27× (z +14.0) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 5 µM 0.289× (z -11.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 56.7 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +14.4) | — |
| [[KATO III (line)]] | alt | 63.3 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +12.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 70.1 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +9.2) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -12.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.23× (z +11.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 49.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -11.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 118 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 64.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -9.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 75.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 58.6 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.42× (z +11.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.4) | — |
| [[SW48 (line)]] | wt | 67.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 53.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +12.4) | — |
| [[C32 (line)]] | wt | 88.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 52.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +20.6) | — |
| [[COLO 205 (line)]] | alt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 44.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +21.2) | — |
| [[NCI-H2347 (line)]] | alt | 67.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.0) | — |
| [[CHP-212 (line)]] | wt | 99.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9997), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDB2]] | +0.76 | +0.76 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_DNA_REPAIR |
| [[PPM1D]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[PHPT1]] | +0.72 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[FDXR]] | +0.69 | +0.60 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[IKBIP]] | +0.65 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[GRIN2C]] | +0.63 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[ANKRA2]] | +0.61 | +0.64 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[ZNF654]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ACER2]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[FUT11]] | +0.59 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[TYMSOS]] | +0.59 | +0.57 / +0.74 | both halves | 9e-06 |  |
| [[GPX1]] | +0.58 | +0.43 / +0.63 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDC]] | -0.62 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[ELAC2]] | -0.61 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[CCT2]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[CCT5]] | -0.57 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[GPN1]] | -0.55 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[CCT3]] | -0.54 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[PSMG1]] | -0.54 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[CHCHD3]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[AGPS]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[POGK]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CCDC91]] | -0.52 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[PRELID3B]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTA2]] | B | ACTA2 activity raises POLH's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without ACTA2 | 0.005 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[PINCR]] | B | PINCR activity weakens POLH's drug response | lines that do not express PINCR (28) vs lines expressing it (20) | the lines without PINCR respond 1.09× as strongly (z diff -0.55); strongest at Panobinostat 0.5 µM: 2.79x vs 1.85x (z diff -3.5) | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; artifact flags |
| [[FDXR]] | B | FDXR activity raises POLH's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without FDXR | 0.012 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[TP53INP1]] | B | TP53INP1 activity raises POLH's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without TP53INP1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers POLH's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EDA2R]] | B | EDA2R activity raises POLH's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.32× lower at baseline in the lines without EDA2R | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[TOP1]] | B | TOP1 activity lowers POLH's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises POLH's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TYMSOS]] | C | TYMSOS activity raises POLH's level | lines that do not express TYMSOS (3) vs lines expressing it (47) | 1.84× lower at baseline in the lines without TYMSOS | 0.099 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: FOXP4-AS1, ENSG00000261341, CCNP; maybe low, not absent |
| [[TP53]] | C | TP53 activity weakens POLH's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 1.00× as strongly (z diff -0.29); strongest at Belinostat 5 µM: 2.83x vs 1.71x (z diff -3.9) | 0.104 over the table, 0.003 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EED]] | C | POLH's natural level strengthens EED's drug response | POLH's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.10; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.4, 36.4); signed map (41.7, -25.2). **Vector** length 127, 42.4% of its response variance represented; |z| ≥ 3 in 1,468 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.9 | +7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +12.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.6 | +10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.5 | +9.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +11.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.3 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.4 | +2.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.8 | +1.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -9.8 | -6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -9.2 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -8.9 | -5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.5 | -7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.0 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.0 | -4.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase eta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,576,185-43,620,523 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XPV, RAD30A, XP-V |
| Gene groups (HGNC) | DNA polymerases; Xeroderma pigmentosum complementation groups; Zinc fingers UBZ3 CCHH-type |
| Hallmark sets | DNA_REPAIR, P53_PATHWAY |
| Reactome | 15 pathways, smallest: Somatic hypermutation of immunoglobulin genes by error-prone base excision repair (BER); Translesion Synthesis by POLH; Somatic hypermutation of immunoglobulin genes by error-prone mismatch repair (MMR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y253](https://www.uniprot.org/uniprotkb/Q9Y253) (DNA polymerase eta):

> DNA polymerase specifically involved in the DNA repair by translesion synthesis (TLS). Due to low processivity on both damaged and normal DNA, cooperates with the heterotetrameric (REV3L, REV7, POLD2 and POLD3) POLZ complex for complete bypass of DNA lesions. Inserts one or 2 nucleotide(s) opposite the lesion, the primer is further extended by the tetrameric POLZ complex. In the case of 1,2-intrastrand d(GpG)-cisplatin cross-link, inserts dCTP opposite the 3' guanine. Particularly important for …

**Summary**, from NCBI Gene [5429](https://www.ncbi.nlm.nih.gov/gene/5429):

> This gene encodes a member of the Y family of specialized DNA polymerases. It copies undamaged DNA with a lower fidelity than other DNA-directed polymerases. However, it accurately replicates UV-damaged DNA; when thymine dimers are present, this polymerase inserts the complementary nucleotides in the newly synthesized DNA, thereby bypassing the lesion and suppressing the mutagenic effect of UV-induced DNA damage. This polymerase is thought to be involved in hypermutation during immunoglobulin …

**Accessions** — [HGNC:9181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9181) · Entrez [5429](https://www.ncbi.nlm.nih.gov/gene/5429) · UniProt [Q9Y253](https://www.uniprot.org/uniprotkb/Q9Y253) · Ensembl [ENSG00000170734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170734)

## Data

Gene col 9997: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9997); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9997, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9997]; `tensor/DDL_lfc|DDL_z.npy` [9997]; `embed/gene_vectors.npy` [9997]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9997 or target_col == 9997). Every well: [[POLH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/POLH.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
