---
symbol: "MEF2D"
type: "gene"
col: 3810
ensembl_id: "ENSG00000116604"
name: "myocyte enhancer factor 2D"
location: "1q22"
module: 1
arm: "-"
pooled_cpm: 87.58
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 27
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001", "written"]
generated_by: "tahoemap"
---

# MEF2D

*myocyte enhancer factor 2D* — 1q22

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> MEF2D is the most broadly expressed member of the MEF2 family, a MADS-box factor that partners myogenic bHLH proteins to drive late muscle differentiation and is a recurrent fusion partner in B-cell acute lymphoblastic leukaemia.

## What it is

MEF2D shares the architecture described for [[MEF2C]]: a MADS box plus MEF2 domain for DNA binding at the A/T-rich MEF2 consensus, dimerisation and cofactor contact. It binds the same sites as its paralogues and is likewise held inactive by class IIa histone deacetylases (HDAC4, [[HDAC5]], HDAC7, HDAC9) until kinase signalling exports those repressors from the nucleus.

What distinguishes MEF2D is breadth. [[MEF2C]] is restricted to muscle, heart, brain and parts of the immune system; MEF2D is expressed in most tissues, making it the family member most likely to be present in a non-muscle cell. Within muscle it is required late rather than early, acting on differentiation and maturation alongside myogenin and MYF6 rather than on determination. A muscle-specific alternatively spliced exon in its transactivation region switches it from an HDAC-bound repressive form to an activating form during differentiation, so MEF2D's identity as activator or repressor is set by splicing as well as by cofactors — one of the clearest cases in the family of a factor whose transcript abundance says little about its output.

Outside muscle, MEF2D supports neuronal survival and activity-dependent transcription, and it is a genuine oncogene in leukaemia: recurrent rearrangements fuse MEF2D to BCL9, HNRNPUL1, CSF1R, DAZAP1 or SS18, producing a high-risk B-ALL subtype with raised MEF2D activity and sensitivity to HDAC inhibition.

## What is uncertain

Which MEF2 paralogue occupies the TRIM72 promoter in a cell is not established; the reporter experiments demonstrated a working MEF2 site, not which family member occupies it. For MEF2D the inference problem is sharper than for its relatives: it is expressed here rather than absent, so a score can be computed, but HDAC gating plus the repressive-versus-activating splice choice leaves the transcript carrying almost no information about whether the protein is doing anything. Its regulon is drawn from muscle, neuronal and lymphoid work and overlaps generic differentiation targets, so a correlation can appear without MEF2D being involved — which is why the principal-component and overlap-removal variants matter more for this gene than for most. Nothing here perturbs MEF2D, so no causal claim is available in either direction.

## References

- Molkentin et al., 1995, Cell — established the cooperative MADS–bHLH mechanism shared by MEF2 family members with myogenic bHLH factors.
- McKinsey et al., 2000, Nature — class II HDAC nuclear export as the switch that releases MEF2 during muscle differentiation.
- Potthoff and Olson, 2007, Development — review covering MEF2 paralogue expression breadth and combinatorial control.
- Jung and Ko, 2010, Biochemical and Biophysical Research Communications — functional MEF2 site juxtaposed to an E-box in the TRIM72 promoter, synergistically activated with MyoD or myogenin.
- Gu et al., 2016, Nature Communications — recurrent MEF2D fusions define a high-risk B-ALL subtype with increased MEF2D activity and HDAC inhibitor sensitivity.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.39× (z +5.3, q 8e-05, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.398× (z -14.9, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.717× (z -7.3, q 3e-11, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP5K]] (+0.70, fdr 7e-06), [[HDAC5]] (+0.67, fdr 8e-06), [[ATG2A]] (+0.64, fdr 2e-05); moves opposite to [[SUCLG2]] (-0.64, fdr 3e-05), [[UTP20]] (-0.63, fdr 7e-06), [[ABCE1]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3810.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +5.3 | 8e-05 | 28/48 (SW480, C32, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +5.1 | 8e-05 | 30/48 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +3.8 | 0.024 | 24/49 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3810.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.398×** | -14.9 | 0e+00 | 45/49 (SW1417, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.417×** | -13.6 | 2e-39 | 36/43 (SHP-77, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.559×** | -9.4 | 1e-18 | 41/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.619×** | -7.5 | 1e-11 | 40/47 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.717×** | -7.3 | 3e-11 | 31/48 (hTERT-HPNE, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.644×** | -7.1 | 1e-10 | 36/48 (NCI-H23, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.622×** | -7.1 | 1e-10 | 33/45 (RPMI-7951, H4, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.668×** | -6.3 | 2e-08 | 33/48 (SNU-423, SW 900, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.476×** | -6.3 | 2e-08 | 44/48 (NCI-H2347, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.675×** | -6.1 | 6e-08 | 29/48 (NCI-H2347, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.486×** | -6.1 | 6e-08 | 39/48 (NCI-H2347, H4, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.681×** | -6.0 | 1e-07 | 36/50 (hTERT-HPNE, LOX-IMVI, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.525×** | -5.4 | 2e-06 | 34/48 (A498, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.777×** | -5.4 | 2e-06 | 28/49 (SHP-77, CHP-212, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.708×** | -5.4 | 3e-06 | 33/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.796×** | -5.1 | 1e-05 | 29/48 (HS-578T, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.744×** | -4.8 | 6e-05 | 29/48 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.744×** | -4.6 | 1e-04 | 26/47 (H4, SW 900, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.616×** | -4.1 | 0.001 | 28/48 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.654×** | -3.6 | 0.008 | 24/48 (NCI-H2347, Hs 766T, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.804×** | -3.3 | 0.019 | 23/48 (NCI-H23, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.816×** | -3.3 | 0.021 | 19/48 (SHP-77, NCI-H1573, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.703×** | -3.0 | 0.058 | 20/49 (NCI-H1792, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 123 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.453× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 120 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -16.1) |
| [[H4 (line)]] | wt | 108 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -8.7) |
| [[HOP62 (line)]] | alt | 86.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -14.6) |
| [[LOX-IMVI (line)]] | wt | 99.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.490× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 176 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 109 | 2 (2 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.72× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 115 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0811× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.331× (z -9.4) |
| [[SW 900 (line)]] | alt | 179 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.334× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 144 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 90.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.8) |
| [[A-427 (line)]] | wt | 88.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 157 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 47.9 | 0 | 2 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.239× (z -9.4) |
| [[HS-578T (line)]] | alt | 60.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 90.2 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.331× (z -9.7) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 92.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.8) |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0657× (z -13.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 81.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[RPMI-7951 (line)]] | alt | 93.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SNU-423 (line)]] | alt | 85.2 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -12.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW1417 (line)]] | alt | 83.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 80.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[C32 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HEC-1-A (line)]] | alt | 46.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[Hs 766T (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 78.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 47.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0754× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 57.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[NCI-H23 (line)]] | alt | 173 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -10.4) |
| [[RKO (line)]] | wt | 45.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SK-MEL-2 (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 87.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP5K]] | +0.70 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[HDAC5]] | +0.67 | +0.57 / +0.64 | both halves | 8e-06 | pathway: HALLMARK_MYOGENESIS; STRING 936 |
| [[ATG2A]] | +0.64 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[FBXO33]] | +0.62 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PHF1]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PRAF2]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[KMT5C]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[RETREG2]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SERTAD3]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[MTMR14]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.58 | +0.64 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUCLG2]] | -0.64 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[UTP20]] | -0.63 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[ABCE1]] | -0.62 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[GCFC2]] | -0.59 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[METTL8]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[QSER1]] | -0.57 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[YTHDC2]] | -0.57 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[SNX5]] | -0.56 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[DNAJC11]] | -0.56 | -0.59 / -0.49 | both halves | 1e-05 | pathway: Mitochondrial biogenesis |
| [[MBTPS2]] | -0.56 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.56 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.56 | -0.62 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MEF2D's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (6.7, -43.3); signed map (-21.3, 12.2). **Vector** length 123, 39.2% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.1 | +5.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.9 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.9 | +2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +5.3 | -5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.0 | -1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.9 | +0.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.9 | +1.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.8 | +1.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.9 | -9.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.4 | -6.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.2 | -5.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.2 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -7.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -4.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | myocyte enhancer factor 2D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,463,727-156,500,779 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Myocyte enhancer factor 2 proteins; MADS box family |
| Hallmark sets | MYOGENESIS |
| Reactome | 15 pathways, smallest: Myogenesis; Expression of BMAL (ARNTL), CLOCK, and NPAS2; NGF-stimulated transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14814](https://www.uniprot.org/uniprotkb/Q14814) (Myocyte-specific enhancer factor 2D):

> Transcriptional activator which binds specifically to the MEF2 element, 5'-YTA[AT](4)TAR-3', found in numerous muscle-specific, growth factor- and stress-induced genes. Mediates cellular functions not only in skeletal and cardiac muscle development, but also in neuronal differentiation and survival. Plays diverse roles in the control of cell growth, survival and apoptosis via p38 MAPK signaling in muscle-specific and/or growth factor-related transcription. Plays a critical role in the …

**Summary**, from NCBI Gene [4209](https://www.ncbi.nlm.nih.gov/gene/4209):

> This gene is a member of the myocyte-specific enhancer factor 2 (MEF2) family of transcription factors. Members of this family are involved in control of muscle and neuronal cell differentiation and development, and are regulated by class II histone deacetylases. Fusions of the encoded protein with Deleted in Azoospermia-Associated Protein 1 (DAZAP1) due to a translocation have been found in an acute lymphoblastic leukemia cell line, suggesting a role in leukemogenesis. The encoded protein may …

**Accessions** — [HGNC:6997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6997) · Entrez [4209](https://www.ncbi.nlm.nih.gov/gene/4209) · UniProt [Q14814](https://www.uniprot.org/uniprotkb/Q14814) · Ensembl [ENSG00000116604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116604)

## Data

Gene col 3810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3810); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3810]; `tensor/DDL_lfc|DDL_z.npy` [3810]; `embed/gene_vectors.npy` [3810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3810 or target_col == 3810). Every well: [[MEF2D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/MEF2D.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
