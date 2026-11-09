---
symbol: "MDM4"
type: "gene"
col: 12630
ensembl_id: "ENSG00000198625"
name: "MDM4 regulator of p53"
location: "1q32.1"
module: 28
arm: "+"
pooled_cpm: 103.78
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/028", "written"]
generated_by: "tahoemap"
---

# MDM4

*MDM4 regulator of p53* — 1q32.1

> [!summary] In one line
> MDM4 — better known in the literature as MDMX or HDMX — is MDM2's paralogue and the second brake on p53: it occludes p53's transactivation domain but, unlike MDM2, is not itself an efficient ubiquitin ligase for p53.

## What it is

MDM4 is built on the same plan as [[MDM2]]: an N-terminal pocket binding the p53 transactivation domain, a central acidic region, and a C-terminal RING. It was found as MDMX, a p53-binding protein with some of MDM2's functional properties.

The asymmetry is at the RING. MDM4's has little demonstrable intrinsic ligase activity toward p53, and instead heterodimerises with MDM2's RING to stimulate MDM2-dependent p53 ubiquitination. MDM4 therefore restrains p53 by two largely non-catalytic routes — blocking the transactivation domain, and setting how well MDM2 works.

Like *Mdm2*-null, *Mdm4*-null embryos die and are rescued by loss of *Trp53*, so MDM4's essential job is also p53 restraint — but the null phenotype differs in timing and tissue bias, read as evidence for non-overlapping control rather than redundancy.

In cancer MDM4 is amplified and overexpressed rather than mutated, concentrated as with MDM2 in tumours that retain wild-type TP53 — retinoblastoma, glioma, and cutaneous melanoma, where it was argued to be a therapeutic target. Splicing is distinctive to this gene: skipping exon 6 yields an unstable short isoform at the expense of full-length protein, and forcing that skipping with antisense oligonucleotides restrains tumour growth — a mechanism with no close MDM2 parallel.

Transcriptionally MDM4 is mostly constitutive, driven from its upstream P1 promoter, but a p53-responsive promoter in the first intron drives a longer isoform, giving MDM4 a weaker version of MDM2's feedback topology.

## What is uncertain

Whether MDM4's RING has any physiologically meaningful ligase activity toward p53 on its own has been argued both ways; the safe statement is that its contribution to p53 turnover runs mainly through MDM2. The division of labour between the paralogues is genuinely unsettled: the differing null phenotypes are compatible with distinct functions and with one function deployed at different times and places, and the literature reads them both ways. MDM4 sits at 1q32, in an arm gained in many epithelial cancers, so an "MDM4 amplification" in copy-number data is often a passenger of 1q gain; attributing a phenotype to MDM4 needs functional experiments, not copy number. The intronic p53-responsive promoter rests on limited work, and how much of total MDM4 mRNA it contributes in an ordinary cell is not established. Finally, a practical caution: most primary papers call this gene MDMX or HDMX, so a literature search on the approved symbol alone misses much of its own literature.

## References

- Shvarts et al., 1996, The EMBO Journal — identified MDMX as a p53-binding protein with some functional properties of MDM2.
- Parant et al., 2001, Nature Genetics — rescue of *Mdm4*-null embryonic lethality by loss of *Trp53*, argued to indicate a pathway not overlapping MDM2's.
- Linares et al., 2003, PNAS — HdmX stimulates Hdm2-mediated ubiquitination and degradation of p53.
- Phillips et al., 2010, Journal of Biological Chemistry — a functional p53-responsive promoter in the first intron drives the longer HDMX-L isoform.
- Gembarska et al., 2012, Nature Medicine — MDM4 as a therapeutic target in cutaneous melanoma.
- Dewaele et al., 2016, Journal of Clinical Investigation — antisense-driven MDM4 exon 6 skipping lowers full-length MDM4 and impairs tumour growth.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +17.2, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.411× (z -29.6, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00174]] (+0.67, fdr 8e-06), [[OCIAD1]] (+0.66, fdr 1e-05), [[ZNF502]] (+0.66, fdr 7e-06); moves opposite to [[GNB2]] (-0.60, fdr 1e-05), [[TPI1]] (-0.56, fdr 5e-05), [[RNF38]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +17.2 | 0e+00 | 37/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.89×** | +16.7 | 0e+00 | 46/49 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.95×** | +13.3 | 3e-38 | 46/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +9.6 | 1e-19 | 39/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +8.3 | 1e-14 | 34/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +7.2 | 4e-11 | 30/48 (NCI-H1573, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +5.3 | 1e-05 | 25/48 (SW 900, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +5.1 | 3e-05 | 30/48 (SW480, C-33 A, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.16× | +4.9 | 5e-05 | 16/48 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.20×** | +4.4 | 6e-04 | 21/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +4.1 | 0.002 | 20/48 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.19× | +4.0 | 0.002 | 14/47 (NCI-H460, SNU-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.014 | 19/49 (A-427, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Hexylresorcinol (drug)]] 5 µM |  | 1.11× | +3.4 | 0.028 | 1/49 (CHP-212) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.3 | 0.036 | 2/48 (LoVo, A-427) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.041 | 15/48 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.070 | 20/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12630.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.411×** | -29.6 | 0e+00 | 48/49 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.582×** | -12.7 | 1e-34 | 45/48 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -11.9 | 3e-30 | 39/48 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.621×** | -11.2 | 6e-27 | 44/48 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -10.4 | 3e-23 | 41/50 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.656×** | -9.9 | 3e-21 | 39/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.761×** | -9.1 | 1e-17 | 33/48 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.685×** | -8.9 | 4e-17 | 41/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.781×** | -5.8 | 4e-07 | 28/48 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.866× | -4.8 | 1e-04 | 15/48 (A-427, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.680×** | -4.7 | 1e-04 | 30/49 (SK-MEL-2, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -4.3 | 8e-04 | 17/48 (J82, A498, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.845× | -3.9 | 0.003 | 20/48 (CHP-212, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.877× | -3.8 | 0.005 | 12/48 (MIA PaCa-2, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.856× | -3.6 | 0.011 | 13/48 (NCI-H460, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 148 | 6 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +19.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -29.4) |
| [[NCI-H1573 (line)]] | alt | 114 | 5 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -16.3) |
| [[NCI-H23 (line)]] | alt | 107 | 2 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -14.2) |
| [[SW480 (line)]] | alt | 94.4 | 5 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -20.5) |
| [[A498 (line)]] | wt | 102 | 4 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +18.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -20.6) |
| [[PANC-1 (line)]] | alt | 126 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -18.9) |
| [[A-427 (line)]] | wt | 88.9 | 3 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.17× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.385× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -12.1) |
| [[SNU-423 (line)]] | alt | 102 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -19.8) |
| [[C32 (line)]] | wt | 173 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -19.3) |
| [[NCI-H2030 (line)]] | alt | 75.9 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -16.1) |
| [[A-172 (line)]] | wt | 110 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -18.3) |
| [[HEC-1-A (line)]] | alt | 100 | 2 | 3 | [[PH-797804 (drug)]] 5 µM 5.19× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -22.2) |
| [[MIA PaCa-2 (line)]] | alt | 129 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.17× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -15.3) |
| [[Panc 03.27 (line)]] | alt | 87.1 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -18.6) |
| [[A549 (line)]] | wt | 104 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +16.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 73.1 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +18.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -14.6) |
| [[BT-474 (line)]] | alt | 87.7 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -9.9) |
| [[COLO 205 (line)]] | alt | 90.2 | 3 | 1 | [[TAK-901 (drug)]] 5 µM 10.1× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -12.3) |
| [[H4 (line)]] | wt | 113 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -16.1) |
| [[HOP62 (line)]] | alt | 76.8 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.02× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -16.5) |
| [[Hs 766T (line)]] | wt | 75.8 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -11.9) |
| [[J82 (line)]] | alt | 90.4 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 100 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 4.57× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -15.8) |
| [[LS 180 (line)]] | wt | 113 | 2 | 2 | [[PH-797804 (drug)]] 5 µM 5.66× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -18.4) |
| [[SK-MEL-2 (line)]] | alt | 135 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -12.2) |
| [[SNU-1 (line)]] | wt | 146 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.39× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 88.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -18.6) |
| [[HS-578T (line)]] | alt | 55.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -11.9) |
| [[HT-29 (line)]] | alt | 96.1 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 3.91× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -21.3) |
| [[LoVo (line)]] | wt | 106 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.40× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -15.5) |
| [[RKO (line)]] | wt | 156 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 4.43× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -19.5) |
| [[RPMI-7951 (line)]] | alt | 104 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -15.3) |
| [[SW 900 (line)]] | alt | 125 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -12.3) |
| [[C-33 A (line)]] | alt | 136 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -14.1) |
| [[CHP-212 (line)]] | wt | 186 | 0 | 2 | — | [[Capmatinib (drug)]] 5 µM 0.0819× (z -10.4) |
| [[HCT15 (line)]] | alt | 149 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 95.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -13.4) |
| [[AN3 CA (line)]] | alt | 97.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 66.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -13.6) |
| [[KATO III (line)]] | alt | 84.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 84.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -11.7) |
| [[SHP-77 (line)]] | alt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -19.4) |
| [[SW1417 (line)]] | alt | 76.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -13.2) |
| [[SW48 (line)]] | wt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 69.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00174]] | +0.67 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[OCIAD1]] | +0.66 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[ZNF502]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZSCAN21]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[RPF2]] | +0.64 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[NOL8]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[RAD50]] | +0.64 | +0.52 / +0.56 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[TYW5]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[MRRF]] | +0.63 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[CHURC1]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[TAF1]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 | pathway: Regulation of TP53 Activity |
| [[GTF2H3]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB2]] | -0.60 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[TPI1]] | -0.56 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[RNF38]] | -0.55 | -0.50 / -0.42 | both halves | 4e-05 | same gene group |
| [[PDE7A]] | -0.55 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[STRN]] | -0.54 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[TMED4]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[MPZL1]] | -0.54 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[PPP2R5E]] | -0.54 | -0.41 / -0.48 | both halves | 4e-05 | pathway: Cell Cycle Checkpoints |
| [[RUSC1]] | -0.53 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[CNOT6L]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[PLEKHA8]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[HDAC3]] | -0.53 | -0.40 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MDM4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises MDM4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises MDM4's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.558). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.5, 5.2); signed map (4.9, -24.3). **Vector** length 114, 34.7% of its response variance represented; |z| ≥ 3 in 1,251 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.2 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.7 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.5 | +2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +17.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.8 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.3 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +13.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +1.9 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -10.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -29.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.5 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -9.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | +0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +2.0 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | MDM4 regulator of p53 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:204,516,379-204,558,120 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDMX, HDMX |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers RANBP2-type; RING finger E3 ubiquitin protein ligases |
| Reactome | 19 pathways, smallest: Regulation of TP53 Activity through Methylation; Oncogene Induced Senescence; Regulation of TP53 Degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [O15151](https://www.uniprot.org/uniprotkb/O15151) (Protein Mdm4):

> Contributes to p53/TP53 regulation. Inhibits p53/TP53- and p73/TP73-mediated cell cycle arrest and apoptosis by binding their transcriptional activation domains. Inhibits degradation of MDM2. Can reverse MDM2-targeted degradation of TP53 while maintaining suppression of TP53 transactivation and apoptotic functions.

**Summary**, from NCBI Gene [4194](https://www.ncbi.nlm.nih.gov/gene/4194):

> This gene encodes a nuclear protein that contains a p53 binding domain at the N-terminus and a RING finger domain at the C-terminus, and shows structural similarity to p53-binding protein MDM2. Both proteins bind the p53 tumor suppressor protein and inhibit its activity, and have been shown to be overexpressed in a variety of human cancers. However, unlike MDM2 which degrades p53, this protein inhibits p53 by binding its transcriptional activation domain. This protein also interacts with MDM2 …

**Accessions** — [HGNC:6974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6974) · Entrez [4194](https://www.ncbi.nlm.nih.gov/gene/4194) · UniProt [O15151](https://www.uniprot.org/uniprotkb/O15151) · Ensembl [ENSG00000198625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198625)

## Data

Gene col 12630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12630); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12630]; `tensor/DDL_lfc|DDL_z.npy` [12630]; `embed/gene_vectors.npy` [12630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12630 or target_col == 12630). Every well: [[MDM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/MDM4.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
