---
symbol: "FANCD2"
type: "gene"
col: 6892
ensembl_id: "ENSG00000144554"
name: "FA complementation group D2"
location: "3p25.3"
module: 6
arm: "+"
pooled_cpm: 43.66
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/006", "written"]
generated_by: "tahoemap"
---

# FANCD2

*FA complementation group D2* — 3p25.3

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> FANCD2 is the Fanconi anaemia protein that, once monoubiquitinated and paired with FANCI, clamps onto DNA at stalled replication forks and licenses interstrand crosslink repair.

## What it is

FANCD2 was positionally cloned as the FA-D2 gene, and its central event was identified at the same time: the FA core complex, through its FANCL ligase, attaches a single ubiquitin to FANCD2 at K561 and to its paralogue FANCI. The modified ID2 heterodimer closes around DNA as a clamp, and that species recruits the steps that unhook a crosslink. Ubiquitination depends on ATR-driven replication-stress signalling and is reversed by USP1-UAF1 ([[USP1]]), so the pathway cycles rather than latching. FANCD2 foci are a standard readout of replication stress. It also protects nascent DNA at stalled forks, a function shared with [[BRCA2]]. Biallelic loss causes Fanconi anaemia.

## What is uncertain

Direct repression by p53 is unlikely for this class of gene. In the earlier MG53/p53 study its membership of the p53 repression arm was also among the less stable across cross-fitting folds. More fundamentally, abundance is the wrong variable: proficiency is set by ubiquitination state, not transcript level, so a modest fall in mRNA at 24 h is not evidence that repair was impaired. As a p53-repressed gene its sign must be flipped before it says anything about p53 output, and any programme membership selected with the TP53 labels is circular ([[Cross-fitting and circularity]]).

## References

- Timmers et al., 2001, Molecular Cell — positional cloning of FANCD2.
- Garcia-Higuera et al., 2001, Molecular Cell — FANCD2 is monoubiquitinated after damage and colocalises with BRCA1, placing the FA proteins in a common pathway.
- Nijman et al., 2005, Molecular Cell — USP1 deubiquitinates FANCD2 and regulates the FA pathway.
- Smogorzewska et al., 2007, Cell — identified FANCI as a monoubiquitinated FANCD2 paralogue required for repair.
- Schlacher et al., 2012, Cancer Cell — FA proteins protect stalled replication forks, a function distinct from crosslink repair.
- Alcón et al., 2020, Nature Structural & Molecular Biology — cryo-EM showing FANCD2-FANCI as a DNA-stabilised clamp.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.81× (z +18.0, q 0e+00, up in 40 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.38× (z +5.8, q 8e-07, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.655× (z -10.9, q 8e-25, down in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.795× (z -5.9, q 5e-07, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLQ]] (+0.88, fdr 7e-06), [[CENPK]] (+0.87, fdr 7e-06), [[BRIP1]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6892.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.81×** | +18.0 | 0e+00 | 40/40 (LoVo, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.61×** | +17.3 | 0e+00 | 42/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.33×** | +14.2 | 3e-43 | 39/42 (NCI-H2347, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.26×** | +5.9 | 6e-07 | 27/47 (SW480, LoVo, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +5.8 | 8e-07 | 24/47 (LoVo, SNU-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~67% of this change | **1.33×** | +5.0 | 6e-05 | 22/46 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.31×** | +4.9 | 7e-05 | 24/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.65×** | +4.7 | 2e-04 | 20/47 (NCI-H2030, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.29×** | +4.5 | 5e-04 | 17/47 (NCI-H23, RKO, …) | two highest doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 1.18× | +4.3 | 8e-04 | 18/47 (SW480, HT-29, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.25×** | +4.0 | 0.003 | 18/46 (SW480, PANC-1, …) | all doses, flat |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.007 | 20/47 (SW480, HT-29, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.8 | 0.007 | 15/33 (HEC-1-A, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.008 | 10/47 (BT-474, NCI-H1573, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.008 | 18/46 (A-427, NCI-H460, …) | all doses, flat |  |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.010 | 16/47 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.015 | 13/47 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.015 | 16/47 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.015 | 11/47 (SW480, KATO III, …) | top dose only | plate-row cell shift |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.048 | 14/47 (SW 900, H4, …) | inconsistent across doses |  |
| [[Methotrexate (drug)]] 5 µM |  | 1.18× | +3.0 | 0.054 | 10/47 (SW480, LS 180, …) | rises with dose |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 1.17× | +2.9 | 0.092 | 10/47 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +2.8 | 0.094 | 14/47 (PANC-1, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.18× | +2.8 | 0.096 | 12/46 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Methotrexate (drug)]] 0.5 µM |  | 1.17× | +2.8 | 0.096 | 10/47 (LS 180, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6892.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.655×** | -10.9 | 8e-25 | 34/47 (A-427, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.583×** | -7.0 | 8e-10 | 29/47 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.684×** | -6.8 | 3e-09 | 31/47 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.795×** | -5.9 | 5e-07 | 23/47 (SW480, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.721×** | -5.6 | 2e-06 | 25/47 (H4, HEC-1-A, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.761×** | -4.9 | 1e-04 | 22/47 (RPMI-7951, NCI-H460, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.765×** | -4.7 | 2e-04 | 20/46 (A-172, HOP62, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.841× | -4.5 | 5e-04 | 13/47 (SW 900, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.782×** | -4.5 | 5e-04 | 20/47 (C-33 A, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 0.845× | -4.3 | 8e-04 | 16/47 (HEC-1-A, SHP-77, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.640×** | -4.2 | 0.001 | 19/41 (HEC-1-A, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.853× | -4.1 | 0.002 | 23/47 (Hs 766T, HCT15, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.799×** | -4.1 | 0.002 | 20/47 (SNU-1, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.795×** | -4.1 | 0.002 | 18/47 (LS 180, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.807×** | -3.9 | 0.004 | 17/47 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.806×** | -3.8 | 0.004 | 22/46 (Hs 766T, NCI-H23, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.826×** | -3.5 | 0.017 | 17/47 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.831×** | -3.4 | 0.024 | 17/47 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.836× | -3.3 | 0.031 | 9/46 (C32, A-172, …) | top dose only |  |
| [[palbociclib (drug)]] 5 µM |  | **0.713×** | -3.2 | 0.035 | 16/46 (SW480, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.848× | -2.9 | 0.084 | 7/47 (MIA PaCa-2, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 156 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.439× (z -10.4) |
| [[H4 (line)]] | wt | 39.4 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0453× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.283× (z -8.9) |
| [[A-172 (line)]] | wt | 43.0 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.325× (z -11.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 69.7 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.268× (z -16.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 36.0 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.325× (z -12.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 36.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.49× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 39.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.00× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SNU-1 (line)]] | wt | 37.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0763× (z -13.9) ⚠ cell-cycle shift, explains ~4% of this change |
| [[C32 (line)]] | wt | 34.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HOP62 (line)]] | alt | 62.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HT-29 (line)]] | alt | 28.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[LoVo (line)]] | wt | 33.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[LOX-IMVI (line)]] | wt | 28.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.87× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Selinexor (drug)]] 5 µM 0.251× (z -12.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 26.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 46.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 35.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[AsPC-1 (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 74.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -9.1) |
| [[HCT15 (line)]] | alt | 61.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.358× (z -9.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HS-578T (line)]] | alt | 26.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[LS 180 (line)]] | wt | 32.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.346× (z -9.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[NCI-H460 (line)]] | wt | 27.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[Panc 03.27 (line)]] | alt | 37.0 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.302× (z -9.0) |
| [[AN3 CA (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 60.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLQ]] | +0.88 | +0.93 / +0.87 | both halves | 7e-06 | STRING 715 |
| [[CENPK]] | +0.87 | +0.85 / +0.91 | both halves | 7e-06 |  |
| [[BRIP1]] | +0.86 | +0.91 / +0.84 | both halves | 7e-06 | same gene group; STRING 997 |
| [[ZGRF1]] | +0.86 | +0.90 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[XRCC2]] | +0.86 | +0.82 / +0.88 | both halves | 7e-06 | same gene group; STRING 799 |
| [[RAD51AP1]] | +0.85 | +0.87 / +0.84 | both halves | 7e-06 | STRING 480 |
| [[GINS1]] | +0.85 | +0.87 / +0.82 | both halves | 7e-06 | STRING 409 |
| [[BRCA1]] | +0.85 | +0.85 / +0.84 | both halves | 7e-06 | same gene group; pathway: TP53 Regulates Transcription of DNA Repair Genes; STRING 999 |
| [[FANCI]] | +0.85 | +0.84 / +0.87 | both halves | 7e-06 | same gene group; pathway: Fanconi Anemia Pathway; STRING 999 |
| [[MCM8]] | +0.85 | +0.81 / +0.87 | both halves | 7e-06 | STRING 526 |
| [[RRM1]] | +0.85 | +0.82 / +0.87 | both halves | 7e-06 |  |
| [[CENPH]] | +0.84 | +0.84 / +0.83 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 6, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises FANCD2's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.48× lower at baseline in the lines without E2F8 | 0.013 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises FANCD2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.48× lower at baseline in the lines without CDC25A | 0.020 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises FANCD2's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without MYBL1 | 0.034 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[ZNF66]] | B | ZNF66 activity raises FANCD2's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.25× lower at baseline in the lines without ZNF66 | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[TCF19]] | B | TCF19 activity raises FANCD2's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.36× lower at baseline in the lines without TCF19 | 0.046 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers FANCD2's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PBK]] | C | PBK activity raises FANCD2's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.45× lower at baseline in the lines without PBK | 0.054 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises FANCD2's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.10× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[AURKB]] | C | AURKB activity raises FANCD2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.58× lower at baseline in the lines without AURKB | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises FANCD2's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 3.05× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.083 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent genes |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises FANCD2's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.26× lower at baseline in the lines without E2F1, MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[MCM10]] | C | MCM10 activity raises FANCD2's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.05× lower at baseline in the lines without MCM10 | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.861). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.8, -46.1); signed map (-39.9, -46.2). **Vector** length 142, 46.6% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.65 to 65); *DNA strand elongation* (reactome, mean cos +0.69 to 28); *DNA Replication* (reactome, mean cos +0.67 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +5.8 | +18.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +5.7 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +5.5 | +17.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +4.9 | +4.9 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +3.8 | +3.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +3.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.5 | +0.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -7.4 | -10.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -6.1 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.6 | -5.6 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.4 | -4.9 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.9 | -3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | FA complementation group D2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:10,026,370-10,101,932 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAD, FA-D2; previously FACD, FANCD |
| Gene groups (HGNC) | FA complementation groups; Armadillo like helical domain containing |
| Reactome | 4 pathways, smallest: Fanconi Anemia Pathway; TP53 Regulates Transcription of DNA Repair Genes; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXW9](https://www.uniprot.org/uniprotkb/Q9BXW9) (Fanconi anemia group D2 protein):

> Required for maintenance of chromosomal stability. Promotes accurate and efficient pairing of homologs during meiosis. Involved in the repair of DNA double-strand breaks, both by homologous recombination and single-strand annealing. The FANCI-FANCD2 complex binds and scans double-stranded DNA (dsDNA) for DNA damage; this complex stalls at DNA junctions between double-stranded DNA and single-stranded DNA (By similarity). May participate in S phase and G2 phase checkpoint activation upon DNA …

**Summary**, from NCBI Gene [2177](https://www.ncbi.nlm.nih.gov/gene/2177):

> The Fanconi anemia complementation group (FANC) currently includes FANCA, FANCB, FANCC, FANCD1 (also called BRCA2), FANCD2, FANCE, FANCF, FANCG, FANCI, FANCJ (also called BRIP1), FANCL, FANCM and FANCN (also called PALB2). The previously defined group FANCH is the same as FANCA. Fanconi anemia is a genetically heterogeneous recessive disorder characterized by cytogenetic instability, hypersensitivity to DNA crosslinking agents, increased chromosomal breakage, and defective DNA repair. The …

**Accessions** — [HGNC:3585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3585) · Entrez [2177](https://www.ncbi.nlm.nih.gov/gene/2177) · UniProt [Q9BXW9](https://www.uniprot.org/uniprotkb/Q9BXW9) · Ensembl [ENSG00000144554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144554)

## Data

Gene col 6892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6892); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6892]; `tensor/DDL_lfc|DDL_z.npy` [6892]; `embed/gene_vectors.npy` [6892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6892 or target_col == 6892). Every well: [[FANCD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/FANCD2.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
