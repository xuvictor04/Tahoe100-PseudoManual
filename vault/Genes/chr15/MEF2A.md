---
symbol: "MEF2A"
type: "gene"
col: 884
ensembl_id: "ENSG00000068305"
name: "myocyte enhancer factor 2A"
location: "15q26.3"
module: 5
arm: "-"
pooled_cpm: 345.59
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/005", "written"]
generated_by: "tahoemap"
---

# MEF2A

*myocyte enhancer factor 2A* — 15q26.3

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> MEF2A is a MADS-box transcription factor of the MEF2 family that drives striated-muscle and activity-dependent neuronal gene programmes, and the MEF2 site it binds is one of the two elements that switch the TRIM72 promoter on during myogenesis.

## What it is

MEF2A carries the family's N-terminal MADS-box and MEF2 domain, which together handle dimerisation and binding to an A/T-rich consensus of the form CTA(A/T)₄TAG, and a C-terminal transactivation domain where almost all of the regulation happens.

MEF2 factors are signal-responsive rather than fate-determining. They do not specify muscle by themselves; they collaborate with the myogenic bHLH factors — MyoD, myogenin — at E-boxes placed next to MEF2 sites. And MEF2 activity is set by repressor occupancy more than by MEF2 abundance: class IIa histone deacetylases (HDAC4, 5, 7, 9) bind the MEF2 domain and hold it silent, and calcium-dependent CaMK signalling phosphorylates them, drives them out of the nucleus, and releases MEF2. p38 MAPK and ERK5 phosphorylate the transactivation domain to activate it; SUMOylation and the corepressor Cabin1 add further control. The practical consequence is that MEF2A protein can be abundant and completely inert.

MEF2A-null mice die perinatally with dilated cardiomyopathy and mitochondrial deficiency, placing MEF2A in the control of cardiac mitochondrial and structural genes. MEF2A is also a central mediator of activity-dependent transcription in neurons, where the same calcium-to-class-IIa-HDAC logic runs on a different target set. Clinically, it came to attention through a reported 21-bp deletion segregating with autosomal-dominant coronary artery disease in one family — a claim that has not held up (see below).

## What is uncertain

The TRIM72 promoter work identified a MEF2 *site*, not a MEF2 *paralogue*. MEF2A, B, C and D share the MADS/MEF2 domain and bind the same consensus, and reporter and gel-shift experiments do not separate them, so "MEF2A drives TRIM72" is an inference from family to member.

Because MEF2 regulation is overwhelmingly post-translational, MEF2A mRNA is a poor proxy for MEF2A activity — the reason its activity is better inferred from its targets, which carries its own assumptions. A regulon built from predominantly non-muscle data may also not contain MEF2A's muscle targets, so inferred MEF2A activity here and MEF2A's myogenic function may not be the same quantity.

On the coronary-artery-disease claim, the honest position is that it failed replication: the deletion was later found in unaffected controls, case-control studies did not reproduce the association, and the original authors contested that reading. MEF2A should not be presented as an established CAD gene.

## References

- Lu et al., 2000, PNAS — signal-dependent activation of MEF2 by dissociation from histone deacetylases.
- Naya et al., 2002, Nature Medicine — MEF2A-null mice show mitochondrial deficiency and cardiac sudden death.
- Wang et al., 2003, Science — reported a MEF2A mutation in an inherited disorder with features of coronary artery disease.
- Weng et al., 2005, Journal of Clinical Investigation — found no MEF2A mutations in coronary artery disease, with the deletion present in unaffected controls.
- Potthoff & Olson, 2007, Development — review of MEF2 as a central regulator of diverse developmental programmes.
- Jung & Ko, 2010, Biochemical and Biophysical Research Communications — TRIM72 is transcriptionally activated by synergism of MyoD (or myogenin) and MEF2 at a conserved MEF2 site adjacent to an E-box.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.30× (z +5.9, q 2e-06, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 6 lines (KATO III 3.08×, BT-474 2.78×, HepG2/C3A 2.66×, LoVo 1.85×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW1417 2.49×, BT-474 1.97×, RKO 1.89×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (A-427 2.20×, hTERT-HPNE 2.47×, RKO 2.19×); [[Tucidinostat (drug)]] 5 µM in 1 line (LS 180 1.61×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.511× (z -15.0, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.860× (z -4.9, q 4e-05, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H2347 0.219×, CFPAC-1 0.170×, SNU-1 0.201×, C32 0.249×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H1792 0.239×, NCI-H2347 0.389×, CFPAC-1 0.315×, Hs 766T 0.322×; ⚠ cell-cycle shift, explains ~20% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.246×, CFPAC-1 0.192×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.458×, CFPAC-1 0.523×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (NCI-H2347 0.509×); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H2347 0.529×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMT2E]] (+0.58, fdr 1e-05), [[DDAH2]] (+0.57, fdr 3e-05), [[RYBP]] (+0.57, fdr 2e-05); moves opposite to [[REXO1]] (-0.59, fdr 1e-05), [[TIMM23B-AGAP6]] (-0.57, fdr 1e-05), [[MCM3AP]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[DAAM1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 884.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 6 lines (KATO III 3.08×, BT-474 2.78×, HepG2/C3A 2.66×, LoVo 1.85×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW1417 2.49×, BT-474 1.97×, RKO 1.89×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (A-427 2.20×, hTERT-HPNE 2.47×, RKO 2.19×); [[Tucidinostat (drug)]] 5 µM in 1 line (LS 180 1.61×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +5.9 | 2e-06 | 27/48 (A-427, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.24×** | +5.0 | 1e-04 | 28/49 (LS 180, SW1417, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.22×** | +4.4 | 0.002 | 25/47 (A-172, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +4.4 | 0.002 | 24/48 (KATO III, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +4.2 | 0.003 | 22/47 (hTERT-HPNE, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.19× | +4.1 | 0.004 | 24/48 (LS 180, C-33 A, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.0 | 0.004 | 12/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.18× | +3.9 | 0.008 | 22/49 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.18× | +3.8 | 0.010 | 18/48 (C-33 A, SW1417, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.12× | +3.7 | 0.013 | 15/48 (SW1417, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.10× | +3.1 | 0.087 | 18/48 (SW1417, BT-474, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.10 | 21/48 (KATO III, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 884.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H2347 0.219×, CFPAC-1 0.170×, SNU-1 0.201×, C32 0.249×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H1792 0.239×, NCI-H2347 0.389×, CFPAC-1 0.315×, Hs 766T 0.322×; ⚠ cell-cycle shift, explains ~20% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.246×, CFPAC-1 0.192×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.458×, CFPAC-1 0.523×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (NCI-H2347 0.509×); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H2347 0.529×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -15.0 | 0e+00 | 41/44 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.577×** | -12.7 | 1e-34 | 46/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.618×** | -10.7 | 1e-24 | 39/47 (CFPAC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.611×** | -10.6 | 6e-24 | 37/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.790×** | -7.7 | 1e-12 | 26/49 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.733×** | -7.2 | 6e-11 | 35/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.770×** | -6.1 | 1e-07 | 30/48 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.650×** | -5.2 | 1e-05 | 28/38 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.859× | -5.0 | 4e-05 | 15/48 (HT-29, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.860× | -4.9 | 4e-05 | 21/48 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -4.5 | 3e-04 | 0/50 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.817×** | -4.5 | 3e-04 | 23/50 (C32, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | **0.830×** | -4.3 | 7e-04 | 22/48 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.836× | -4.1 | 0.001 | 23/48 (CFPAC-1, C32, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.839× | -4.1 | 0.002 | 20/48 (SW 1271, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.873× | -3.1 | 0.052 | 15/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 5 µM |  | **0.777×** | -3.1 | 0.067 | 20/46 (AN3 CA, A498, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.872× | -3.0 | 0.068 | 9/49 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.880× | -2.9 | 0.087 | 15/48 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.881× | -2.9 | 0.090 | 14/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 781 | 0 | 18 (15 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.523× (z -10.5) |
| [[C32 (line)]] | wt | 591 | 0 | 15 (15 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -17.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 1,367 | 0 | 13 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -17.5) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.458× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 562 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.509× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 745 | 0 | 10 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -23.4) ⚠ cell-cycle shift, explains ~20% of this change |
| [[HOP62 (line)]] | alt | 336 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 267 | 3 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +16.9) | [[Dinaciclib (drug)]] 0.05 µM 0.444× (z -11.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 492 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -16.2) ⚠ cell-cycle shift, explains ~20% of this change |
| [[RPMI-7951 (line)]] | alt | 641 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[BT-474 (line)]] | alt | 166 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +13.6) | — |
| [[HT-29 (line)]] | alt | 325 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -13.4) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 296 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.498× (z -12.2) ⚠ cell-cycle shift, explains ~1% of this change |
| [[PANC-1 (line)]] | alt | 407 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -16.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 301 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HepG2_C3A (line)]] | wt | 212 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 257 | 3 (2 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.61× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.477× (z -11.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 321 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.281× (z -14.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 168 | 2 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.20× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -14.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 277 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.504× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[CHP-212 (line)]] | wt | 792 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -16.0) ⚠ cell-cycle shift, explains ~20% of this change |
| [[HCT15 (line)]] | alt | 332 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -13.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 386 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.523× (z -10.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 294 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.19× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 257 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.47× (z +11.3) | — |
| [[J82 (line)]] | alt | 238 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -16.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 282 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.517× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 191 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -12.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 225 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.523× (z -8.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 353 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.504× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 336 | 1 | 1 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.74× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -18.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 230 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -9.5) ⚠ cell-cycle shift, explains ~66% of this change |
| [[SW480 (line)]] | alt | 264 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.532× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 297 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 176 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.53× (z +8.8) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[A549 (line)]] | wt | 272 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -10.2) ⚠ cell-cycle shift, explains ~20% of this change |
| [[HEC-1-A (line)]] | alt | 290 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.500× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 264 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 516 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 218 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.485× (z -9.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 331 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 306 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 309 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 243 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 422 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 354 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 262 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2E]] | +0.58 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[DDAH2]] | +0.57 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[RYBP]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[NPTN]] | +0.56 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ABI1]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PPDPF]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[FNBP1]] | +0.55 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[CRIP2]] | +0.54 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[TEC]] | +0.53 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[KRAS]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 | pathway: Signaling by NTRK1 (TRKA) |
| [[HES4]] | +0.51 | +0.34 / +0.50 | both halves | 1e-04 |  |
| [[VPS37D]] | +0.51 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REXO1]] | -0.59 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | -0.57 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[MCM3AP]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | -0.56 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[POLR3E]] | -0.56 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[WDR4]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ALG8]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[AGAP6]] | -0.53 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[DCTD]] | -0.53 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[DNAJC11]] | -0.53 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[TWNK]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[ZNF202]] | -0.53 | -0.55 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAAM1]] | C | MEF2A's natural level weakens DAAM1's drug response | MEF2A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.74, reverse +0.32; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[FHIP1A]] | C | MEF2A's natural level strengthens FHIP1A's drug response | MEF2A's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.38; direction not clear | 0.079 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.590). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (0.5, -36.4); signed map (-10.2, 15.4). **Vector** length 126, 43.9% of its response variance represented; |z| ≥ 3 in 1,674 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +8.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +6.1 | +3.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.8 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | -10.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.4 | +3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.7 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +1.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -7.1 | -1.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -0.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -4.9 | -6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.5 | -1.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.3 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | myocyte enhancer factor 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:99,565,417-99,716,488 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RSRFC4, RSRFC9 |
| Gene groups (HGNC) | Myocyte enhancer factor 2 proteins; MADS box family |
| Hallmark sets | MYOGENESIS |
| Reactome | 29 pathways, smallest: ERK/MAPK targets; Myogenesis; MAPK targets/ Nuclear events mediated by MAP kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02078](https://www.uniprot.org/uniprotkb/Q02078) (Myocyte-specific enhancer factor 2A):

> Transcriptional activator which binds specifically to the MEF2 element, 5'-YTA[AT](4)TAR-3', found in numerous muscle-specific genes. Also involved in the activation of numerous growth factor- and stress-induced genes. Mediates cellular functions not only in skeletal and cardiac muscle development, but also in neuronal differentiation and survival. Plays diverse roles in the control of cell growth, survival and apoptosis via p38 MAPK signaling in muscle-specific and/or growth factor-related …

**Summary**, from NCBI Gene [4205](https://www.ncbi.nlm.nih.gov/gene/4205):

> The protein encoded by this gene is a DNA-binding transcription factor that activates many muscle-specific, growth factor-induced, and stress-induced genes. The encoded protein can act as a homodimer or as a heterodimer and is involved in several cellular processes, including muscle development, neuronal differentiation, cell growth control, and apoptosis. Defects in this gene could be a cause of autosomal dominant coronary artery disease 1 with myocardial infarction (ADCAD1). Several …

**Accessions** — [HGNC:6993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6993) · Entrez [4205](https://www.ncbi.nlm.nih.gov/gene/4205) · UniProt [Q02078](https://www.uniprot.org/uniprotkb/Q02078) · Ensembl [ENSG00000068305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068305)

## Data

Gene col 884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 884); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 884]; `tensor/DDL_lfc|DDL_z.npy` [884]; `embed/gene_vectors.npy` [884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 884 or target_col == 884). Every well: [[MEF2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/MEF2A.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
