---
symbol: "KIF11"
type: "gene"
col: 6134
ensembl_id: "ENSG00000138160"
name: "kinesin family member 11"
location: "10q23.33"
module: 22
arm: "+"
pooled_cpm: 78.39
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/022", "written"]
generated_by: "tahoemap"
---

# KIF11

*kinesin family member 11* — 10q23.33

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> KIF11 encodes Eg5, the kinesin-5 motor that cross-links antiparallel microtubules and pushes the two halves of the mitotic spindle apart.

## What it is

Eg5 is a homotetramer with motor domains at both ends, so it slides antiparallel microtubules past one another, generating the outward force that separates duplicated centrosomes into a bipolar spindle. Cdk1 phosphorylation of the tail switches on its spindle association at mitotic entry. Inhibit it and cells enter mitosis but collapse into a monopolar spindle — the phenotype that identified monastrol in one of the first small-molecule phenotypic screens, and the basis of the kinesin-spindle-protein inhibitor class, whose single-agent activity in solid tumours disappointed. Its transcript is tightly proliferation-coupled and sits in the canonical E2F/DREAM-regulated cell-cycle cluster. Germline heterozygous loss-of-function mutations cause microcephaly, variably with lymphoedema and chorioretinal dysplasia.

## What is uncertain

KIF11 is not a direct p53 target, and in the earlier MG53/p53 study its direction was flagged as mixed — it moved both ways across compounds — so no single direction is a fact about the gene. Some of that scatter is expected: many compounds in a panel this size perturb the cycle directly, and a transcript this tightly proliferation-coupled reports where cells sit in the cycle as much as what p53 is doing. If any exposure is itself an antimitotic, the arrest it produces would move KIF11 for reasons unrelated to p53.

## References

- Blangy et al., 1995, Cell — showed Cdk1 phosphorylation of Eg5 controls its spindle association and that Eg5 is required for bipolar spindle formation.
- Mayer et al., 1999, Science — identified monastrol as an Eg5 inhibitor in a phenotype-based screen.
- Ostergaard et al., 2012, American Journal of Human Genetics — KIF11 mutations cause microcephaly with lymphoedema and chorioretinopathy.
- Engeland, 2018, Cell Death and Differentiation — review of p53-p21-DREAM-mediated repression of cell-cycle and mitosis genes.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.97× (z +14.4, q 2e-44, up in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~87% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.92× (z +5.1, q 2e-05, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.609× (z -10.6, q 3e-23, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~80% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.604× (z -7.6, q 5e-12, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPG]] (+0.97, fdr 7e-06), [[TPX2]] (+0.94, fdr 7e-06), [[MKI67]] (+0.94, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6134.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.97×** | +14.4 | 2e-44 | 38/48 (PANC-1, A549, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **2.19×** | +11.4 | 2e-27 | 42/48 (PANC-1, C32, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.45×** | +7.1 | 3e-10 | 35/48 (HEC-1-A, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **2.06×** | +5.7 | 2e-06 | 31/47 (J82, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.29×** | +5.4 | 6e-06 | 30/48 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.42×** | +5.3 | 1e-05 | 28/48 (KATO III, LoVo, …) | inconsistent across doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +5.1 | 2e-05 | 25/48 (HEC-1-A, SW1417, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.33×** | +4.3 | 0.001 | 25/47 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.31×** | +4.1 | 0.002 | 22/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.36×** | +4.0 | 0.004 | 22/48 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.29×** | +3.9 | 0.005 | 20/48 (KATO III, C32, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.29×** | +3.8 | 0.007 | 25/48 (AsPC-1, SW 900, …) | all doses, flat | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.048 | 21/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.065 | 16/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6134.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.609×** | -10.6 | 3e-23 | 36/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.486×** | -9.3 | 3e-18 | 41/48 (LOX-IMVI, H4, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.561×** | -8.2 | 4e-14 | 38/48 (LS 180, A-172, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.604×** | -7.6 | 5e-12 | 39/48 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.668×** | -6.1 | 1e-07 | 39/48 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.483×** | -5.7 | 1e-06 | 31/45 (A-172, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.711×** | -5.1 | 2e-05 | 27/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.791×** | -5.0 | 4e-05 | 28/48 (Hs 766T, HCT15, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.797×** | -4.8 | 9e-05 | 26/48 (A-427, LS 180, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.690×** | -4.8 | 9e-05 | 27/48 (Hs 766T, HT-29, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.572×** | -4.4 | 5e-04 | 26/48 (SW 900, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.738×** | -4.4 | 5e-04 | 25/47 (A498, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[palbociclib (drug)]] 5 µM |  | **0.614×** | -3.8 | 0.005 | 22/47 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.783×** | -3.7 | 0.010 | 20/48 (SW 1271, HT-29, …) | two highest doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.760×** | -3.5 | 0.014 | 21/48 (Hs 766T, KATO III, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.847× | -3.5 | 0.014 | 17/48 (MIA PaCa-2, SNU-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.690×** | -3.5 | 0.014 | 21/48 (SW48, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.848× | -3.5 | 0.014 | 18/48 (NCI-H1792, Hs 766T, …) | rises with dose | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.801×** | -3.3 | 0.026 | 20/48 (J82, KATO III, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.860× | -3.2 | 0.035 | 15/48 (COLO 205, HepG2/C3A, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.809×** | -3.2 | 0.035 | 18/47 (A-172, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.667×** | -3.2 | 0.035 | 16/48 (hTERT-HPNE, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **0.691×** | -2.9 | 0.076 | 18/48 (LOX-IMVI, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.77 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6134. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 68.1 | 1 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.6) ⚠ cell-cycle shift, explains ~87% of this change | [[Selinexor (drug)]] 5 µM 0.226× (z -14.8) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.245× (z -9.9) |
| [[LS 180 (line)]] | wt | 63.7 | 0 | 7 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.152× (z -17.4) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.374× (z -9.0) |
| [[A-172 (line)]] | wt | 81.5 | 0 | 6 (5 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.163× (z -11.1) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.399× (z -9.3) |
| [[A-427 (line)]] | wt | 132 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.188× (z -21.5) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.338× (z -14.0) |
| [[A498 (line)]] | wt | 65.5 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.166× (z -22.8) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.427× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 128 | 3 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.3) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.98× (z +8.6) | [[Auranofin (drug)]] 5 µM 0.428× (z -10.2) |
| [[A549 (line)]] | wt | 70.7 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +18.6) ⚠ cell-cycle shift, explains ~87% of this change | [[Selinexor (drug)]] 5 µM 0.469× (z -8.9) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.481× (z -8.6) |
| [[H4 (line)]] | wt | 79.8 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.204× (z -12.6) ⚠ cell-cycle shift, explains ~80% of this change |
| [[BT-474 (line)]] | alt | 44.9 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.234× (z -9.7) |
| [[C32 (line)]] | wt | 61.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +15.3) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[LoVo (line)]] | wt | 40.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +13.3) ⚠ cell-cycle shift, explains ~87% of this change | [[Selinexor (drug)]] 5 µM 0.447× (z -9.5) ⚠ cell-cycle shift, explains ~80% of this change |
| [[PANC-1 (line)]] | alt | 96.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +22.1) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[AN3 CA (line)]] | alt | 264 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 24.6 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +10.8) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[HOP62 (line)]] | alt | 117 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.7) ⚠ cell-cycle shift, explains ~87% of this change | [[Selinexor (drug)]] 5 µM 0.525× (z -8.6) ⚠ cell-cycle shift, explains ~80% of this change |
| [[HS-578T (line)]] | alt | 41.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +15.0) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[NCI-H2347 (line)]] | alt | 73.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +17.8) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[NCI-H460 (line)]] | wt | 76.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.327× (z -12.6) ⚠ cell-cycle shift, explains ~80% of this change |
| [[Panc 03.27 (line)]] | alt | 82.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +16.6) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[RKO (line)]] | wt | 72.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +16.4) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[Hs 766T (line)]] | wt | 73.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.341× (z -11.0) ⚠ cell-cycle shift, explains ~80% of this change |
| [[hTERT-HPNE (line)]] | wt | 35.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +9.7) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[J82 (line)]] | alt | 84.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.7) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[KATO III (line)]] | alt | 75.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 31.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +11.5) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[NCI-H2030 (line)]] | alt | 76.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +16.3) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[SNU-1 (line)]] | wt | 92.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.133× (z -16.6) ⚠ cell-cycle shift, explains ~80% of this change |
| [[SNU-423 (line)]] | alt | 83.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.9) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[SW 900 (line)]] | alt | 93.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.7) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[SW1417 (line)]] | alt | 92.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.3) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[C-33 A (line)]] | alt | 132 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6134), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPG]] | +0.97 | +0.96 / +0.97 | both halves | 7e-06 | STRING 975 |
| [[TPX2]] | +0.94 | +0.95 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 965 |
| [[MKI67]] | +0.94 | +0.92 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 931 |
| [[BIRC5]] | +0.92 | +0.93 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 957 |
| [[KIF23]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 994 |
| [[CCNA2]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 978 |
| [[KIF15]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 983 |
| [[PRC1]] | +0.92 | +0.94 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 972 |
| [[CDK1]] | +0.91 | +0.92 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 987 |
| [[RACGAP1]] | +0.91 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 978 |
| [[KIF4A]] | +0.91 | +0.93 / +0.90 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 952 |
| [[NCAPH]] | +0.91 | +0.90 / +0.93 | both halves | 7e-06 | STRING 908 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises KIF11's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.29× lower at baseline in the lines without PIMREG | 0.010 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises KIF11's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.32× lower at baseline in the lines without E2F8 | 0.019 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises KIF11's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.89× lower at baseline in the lines without MYBL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises KIF11's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.73× lower at baseline in the lines without AURKB | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises KIF11's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.63× lower at baseline in the lines without PBK | 0.037 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises KIF11's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.25× lower at baseline in the lines without NDC80 | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises KIF11's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.75× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent genes |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises KIF11's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 2.90× lower at baseline in the lines without C21orf58, SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises KIF11's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[AURKB]] | C | AURKB activity strengthens KIF11's drug response | lines that do not express AURKB (4) vs lines expressing it (44) | the lines without AURKB respond 0.58× as strongly (z diff +1.67); strongest at Bortezomib 5 µM: 1.27x vs 0.47x (z diff +3.8) | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LRRCC1]] | C | LRRCC1 activity lowers KIF11's level | lines that do not express LRRCC1 (4) vs lines expressing it (46) | 1.92× higher at baseline in the lines without LRRCC1 | 0.092 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.946). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.8, -54.7); signed map (-48.6, -43.9). **Vector** length 171, 64.8% of its response variance represented; |z| ≥ 3 in 1,368 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.74 to 48); *E2F targets* (hallmark, mean cos +0.75 to 46); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.74 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +7.2 | +11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +7.1 | +14.4 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +5.9 | +5.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +5.4 | +5.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +5.0 | +3.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +4.0 | +3.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.2 | +3.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.0 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.9 | +2.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | -9.5 | -8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.4 | -7.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -9.2 | -9.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -8.7 | -10.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -7.8 | -5.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -5.3 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -4.4 | -4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.33 — chr10:92,574,105-92,655,395 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Eg5, HKSP, TRIP5; previously KNSL1 |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 13 pathways, smallest: Kinesins; Processing of antigen in germinal center B cells; COPI-dependent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [P52732](https://www.uniprot.org/uniprotkb/P52732) (Kinesin-like protein KIF11):

> Motor protein required for establishing a bipolar spindle and thus contributing to chromosome congression during mitosis. Required in non-mitotic cells for transport of secretory proteins from the Golgi complex to the cell surface.

**Summary**, from NCBI Gene [3832](https://www.ncbi.nlm.nih.gov/gene/3832):

> This gene encodes a motor protein that belongs to the kinesin-like protein family. Members of this protein family are known to be involved in various kinds of spindle dynamics. The function of this gene product includes chromosome positioning, centrosome separation and establishing a bipolar spindle during cell mitosis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6388) · Entrez [3832](https://www.ncbi.nlm.nih.gov/gene/3832) · UniProt [P52732](https://www.uniprot.org/uniprotkb/P52732) · Ensembl [ENSG00000138160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138160)

## Data

Gene col 6134: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6134); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6134, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6134]; `tensor/DDL_lfc|DDL_z.npy` [6134]; `embed/gene_vectors.npy` [6134]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6134 or target_col == 6134). Every well: [[KIF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/KIF11.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
