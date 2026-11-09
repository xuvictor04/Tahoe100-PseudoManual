---
symbol: "SEMA4A"
type: "gene"
col: 12151
ensembl_id: "ENSG00000196189"
name: "semaphorin 4A"
location: "1q22"
module: 53
arm: "+"
pooled_cpm: 19.45
n_lines_expressing: 42
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 10
direction_downstream: 20
tags: ["gene", "module/053", "written"]
generated_by: "tahoemap"
---

# SEMA4A

*semaphorin 4A* — 1q22

> [!summary] In one line
> SEMA4A encodes semaphorin 4A, a transmembrane class IV semaphorin signalling through plexins, neuropilin-1 and Tim-2, with reported roles in T-cell activation, angiogenesis and photoreceptor survival.

## What it is

A sema domain plus an Ig-like domain on a membrane anchor, so Sema4A acts in trans at cell–cell contact; a shed soluble form also circulates. Its best-supported role is immune: expressed on dendritic cells and macrophages, it enhances T-cell priming and Th1-type differentiation, with Tim-2 reported as the T-cell-side receptor. In the vasculature, endothelial Sema4A signalling through plexin-D1 reportedly dampens VEGF-driven angiogenesis. In the eye, SEMA4A variants were reported in retinitis pigmentosa and cone–rod dystrophy, and mouse work ties it to endosomal sorting in retinal pigment epithelium needed for photoreceptor survival. The through-line: a context-dependent ligand whose output depends on which receptor its partner cell presents.

## What is uncertain

SEMA4A carries the readthrough-geometry flag: it sits within 20 kb 3′ of a much higher-expressed same-strand gene, so some reads credited to it may be that neighbour's ([[Readthrough spillover]]). For a partner gene with the same geometry, a shared-artefact explanation is at least as plausible as a shared regulator. The biology is unsettled too: the immune work rests on mouse systems and a receptor, Tim-2, whose human counterpart is unclear, and the dominant retinal variant from the original genetics paper has since been reassessed as a common polymorphism, so that gene–disease claim is weaker than database entries imply.

## References

- Kumanogoh et al., 2002, Nature — showed that Sema4A enhances T-cell activation and interacts with Tim-2.
- Abid et al., 2006, Journal of Medical Genetics — first reported SEMA4A variants in retinitis pigmentosa and cone–rod dystrophy; the dominant variant has since been questioned.
- Kumanogoh & Kikutani, 2013, Nature Reviews Immunology — review of semaphorin signalling through plexins and neuropilins in immunity.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 10.0× (z +20.3, q 0e+00, up in 34 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.277× (z -4.2, q 0.015, down in 20 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM72]] (+0.82, fdr 7e-06), [[GRAMD2A]] (+0.76, fdr 7e-06), [[C19orf38]] (+0.76, fdr 7e-06); moves opposite to [[PSMF1]] (-0.60, fdr 1e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LSMEM2]] → it (grade B ⚠); 20 go from it, the strongest it → [[FOS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **10.0×** | +20.3 | 0e+00 | 34/37 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.30×** | +10.5 | 2e-23 | 30/38 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.16×** | +8.9 | 1e-16 | 26/38 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.34×** | +7.5 | 7e-12 | 23/39 (A-172, NCI-H460, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.49×** | +7.5 | 7e-12 | 27/38 (SK-MEL-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.43×** | +7.4 | 1e-11 | 26/36 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.65×** | +5.8 | 4e-07 | 23/37 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.13×** | +4.7 | 2e-04 | 22/40 (NCI-H2030, HCT15, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **2.08×** | +4.6 | 3e-04 | 19/40 (SW48, HepG2/C3A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.1 | 0.002 | 19/40 (A-172, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.92×** | +4.1 | 0.003 | 19/40 (C32, NCI-H460, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.85×** | +3.7 | 0.011 | 15/36 (SW48, NCI-H460, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +3.6 | 0.014 | 14/40 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.69×** | +3.3 | 0.043 | 14/37 (A-172, C32, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.69×** | +3.3 | 0.043 | 15/39 (SW 900, AsPC-1, …) | top dose only |  |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.062 | 11/39 (SW 900, HEC-1-A, …) | top dose only | position effect removed |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.70×** | +3.0 | 0.088 | 8/40 (A498, J82, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12151.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.277×** | -4.2 | 0.015 | 20/36 (KATO III, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.639×** | -4.0 | 0.016 | 21/40 (NCI-H1573, HT-29, …) | rises with dose | low cells (technical?); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.538×** | -3.9 | 0.016 | 21/39 (HT-29, KATO III, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.543×** | -3.8 | 0.016 | 19/39 (HT-29, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.652×** | -3.8 | 0.016 | 19/39 (HT-29, KATO III, …) | all doses, flat | position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | **0.539×** | -3.7 | 0.018 | 21/37 (J82, NCI-H23, …) | top dose only |  |
| [[vincristine (drug)]] 0.05 µM |  | **0.566×** | -3.4 | 0.059 | 16/39 (AsPC-1, KATO III, …) | inconsistent across doses | position effect removed |
| [[Afatinib (drug)]] 5 µM |  | **0.596×** | -3.3 | 0.061 | 16/40 (HT-29, H4, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.591×** | -3.3 | 0.061 | 16/40 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.573×** | -3.2 | 0.079 | 12/39 (SW 900, NCI-H1573, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.617× | -3.0 | 0.12 | 13/39 (SW 1088, SW 900, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 14.1 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.58× (z +13.1) | [[Pemetrexed (drug)]] 5 µM 0.0879× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 10.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.7× (z +18.0) | — |
| [[KATO III (line)]] | alt | 40.2 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0490× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Benproperine (phosphate) (drug)]] 5 µM 0.117× (z -8.6) |
| [[HT-29 (line)]] | alt | 81.3 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0420× (z -12.1) |
| [[C32 (line)]] | wt | 25.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 233× (z +16.0) | — |
| [[HEC-1-A (line)]] | alt | 37.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.62× (z +15.9) | — |
| [[LOX-IMVI (line)]] | wt | 8.57 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.6× (z +15.8) | — |
| [[NCI-H1573 (line)]] | alt | 20.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +16.0) | — |
| [[NCI-H23 (line)]] | alt | 7.69 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 69.2× (z +18.1) | — |
| [[NCI-H2347 (line)]] | alt | 7.90 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.12× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 6.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 91.2× (z +17.4) | — |
| [[A498 (line)]] | wt | 34.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.14× (z +10.5) | — |
| [[A549 (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.50× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0567× (z -8.5) |
| [[BT-474 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[CFPAC-1 (line)]] | alt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +12.1) | — |
| [[HS-578T (line)]] | alt | 9.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.7× (z +12.1) | — |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +9.9) | — |
| [[J82 (line)]] | alt | 8.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +12.2) | — |
| [[LoVo (line)]] | wt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +12.9) | — |
| [[NCI-H1792 (line)]] | alt | 6.91 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 79.7× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 26.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 6.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +11.1) | — |
| [[A-427 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.25 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM72]] | +0.82 | +0.84 / +0.79 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.76 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[C19orf38]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[FGF18]] | +0.75 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[PRKCG]] | +0.74 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[PILRA]] | +0.73 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.72 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[INTS6]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[PPP1R36]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[EPHA1-AS1]] | +0.70 | +0.76 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMF1]] | -0.60 | -0.61 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSMEM2]] | B | LSMEM2 activity raises SEMA4A's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 2.95× lower at baseline in the lines without LSMEM2 | 0.019 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[LMO7DN]] | B | LMO7DN activity raises SEMA4A's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 2.39× lower at baseline in the lines without LMO7DN | 0.028 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[TOP2A]] | B | TOP2A activity lowers SEMA4A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC2A9]] | B | SLC2A9 activity raises SEMA4A's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 3.03× lower at baseline in the lines without SLC2A9 | 0.028 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[KRT86]] | B | KRT86 activity raises SEMA4A's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without KRT86 | 0.046 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[MTNR1A]] | B | MTNR1A activity raises SEMA4A's level | lines that do not express MTNR1A (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without MTNR1A | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CFAP45]] | B | CFAP45 activity raises SEMA4A's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 2.76× lower at baseline in the lines without CFAP45 | 0.051 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[C21orf91-OT1]] | B | C21orf91-OT1 activity raises SEMA4A's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 2.59× lower at baseline in the lines without C21orf91-OT1 | 0.052 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[EPHA1-AS1]] | B | EPHA1-AS1 activity raises SEMA4A's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 2.41× lower at baseline in the lines without EPHA1-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[ATAD3C]] | B | ATAD3C activity raises SEMA4A's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 1.66× lower at baseline in the lines without ATAD3C | 0.088 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOS]] | B | SEMA4A activity raises FOS's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.53× lower at baseline in the lines without SEMA4A | 0.024 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[LINC00672]] | B | SEMA4A activity raises LINC00672's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without SEMA4A | 0.030 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[PITRM1-AS1]] | B | SEMA4A activity raises PITRM1-AS1's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without SEMA4A | 0.035 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[TNNT2]] | B | SEMA4A activity raises TNNT2's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.96× lower at baseline in the lines without SEMA4A | 0.038 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[SPTBN5]] | B | SEMA4A activity raises SPTBN5's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.88× lower at baseline in the lines without SEMA4A | 0.041 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[IQCN]] | B | SEMA4A activity raises IQCN's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without SEMA4A | 0.050 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[KRT86]] | B | SEMA4A activity raises KRT86's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 3.02× lower at baseline in the lines without SEMA4A | 0.053 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[PHYHD1]] | B | SEMA4A activity raises PHYHD1's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.74× lower at baseline in the lines without SEMA4A | 0.060 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[MIR23AHG]] | B | SEMA4A activity raises MIR23AHG's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without SEMA4A | 0.060 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[GARIN1A]] | B | SEMA4A activity raises GARIN1A's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without SEMA4A | 0.061 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[TLE4]] | B | SEMA4A activity raises TLE4's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 4.50× lower at baseline in the lines without SEMA4A | 0.072 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[ERI2]] | B | SEMA4A activity raises ERI2's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without SEMA4A | 0.073 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.3, -16.4); signed map (16.3, 11.9). **Vector** length 124, 34.6% of its response variance represented; |z| ≥ 3 in 1,114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +20.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +10.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.4 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +4.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +1.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +3.3 | +3.3 |
| fall | [[NG25 (drug)]] 5 µM |  | -4.5 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -3.4 | -4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.3 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.1 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -1.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,147,366-156,177,752 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SemB, FLJ12287, CORD10; previously SEMAB |
| Gene groups (HGNC) | Semaphorins |
| Reactome | 4 pathways, smallest: Other semaphorin interactions; Semaphorin interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3S1](https://www.uniprot.org/uniprotkb/Q9H3S1) (Semaphorin-4A):

> Cell surface receptor for PLXNB1, PLXNB2, PLXNB3 and PLXND1 that plays an important role in cell-cell signaling (By similarity). Regulates glutamatergic and GABAergic synapse development (By similarity). Promotes the development of inhibitory synapses in a PLXNB1-dependent manner and promotes the development of excitatory synapses in a PLXNB2-dependent manner (By similarity). Plays a role in priming antigen-specific T-cells, promotes differentiation of Th1 T-helper cells, and thereby …

**Summary**, from NCBI Gene [64218](https://www.ncbi.nlm.nih.gov/gene/64218):

> This gene encodes a member of the semaphorin family of soluble and transmembrane proteins. Semaphorins are involved in numerous functions, including axon guidance, morphogenesis, carcinogenesis, and immunomodulation. The encoded protein is a single-pass type I membrane protein containing an immunoglobulin-like C2-type domain, a PSI domain and a sema domain. It inhibits axonal extension by providing local signals to specify territories inaccessible for growing axons. It is an activator of …

**Accessions** — [HGNC:10729](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10729) · Entrez [64218](https://www.ncbi.nlm.nih.gov/gene/64218) · UniProt [Q9H3S1](https://www.uniprot.org/uniprotkb/Q9H3S1) · Ensembl [ENSG00000196189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196189)

## Data

Gene col 12151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12151); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12151]; `tensor/DDL_lfc|DDL_z.npy` [12151]; `embed/gene_vectors.npy` [12151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12151 or target_col == 12151). Every well: [[SEMA4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/SEMA4A.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
