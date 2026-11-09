---
symbol: "CHEK2"
type: "gene"
col: 11452
ensembl_id: "ENSG00000183765"
name: "checkpoint kinase 2"
location: "22q12.1"
module: 67
arm: "+"
pooled_cpm: 39.88
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/067", "written"]
generated_by: "tahoemap"
---

# CHEK2

*checkpoint kinase 2* — 22q12.1

> [!summary] In one line
> CHEK2 encodes CHK2, the checkpoint kinase that ATM activates after DNA double-strand breaks and that phosphorylates p53 and the CDC25 phosphatases to enforce arrest.

## What it is

CHK2 is a serine/threonine kinase built from an N-terminal SQ/TQ cluster, a forkhead-associated (FHA) domain and a C-terminal kinase domain. Its activation is the canonical double-strand-break cascade: ATM phosphorylates T68 in the SQ/TQ cluster, the phosphothreonine is read by the FHA domain of a partner molecule so CHK2 transiently dimerises, autophosphorylation in the activation loop follows, and the kinase disperses as an active monomer. That mechanism makes CHK2 a signal amplifier — a localised ATM signal at a break becomes a diffusible, nucleus-wide kinase activity.

Its substrates define two parallel outputs. CHK2 phosphorylates p53 at S20, which sits in the MDM2-binding surface, and the standard model is that this contributes to p53 stabilisation — placing CHK2 upstream of everything in [[The p53 pathway]]. Independently, CHK2 phosphorylates CDC25A, driving its degradation, and CDC25C, promoting 14-3-3 sequestration; either way CDK-activating phosphatase activity falls and the cell cycle halts without any transcription being required. CHK2 also acts on BRCA1, E2F1 and PML. It is the DSB-responsive counterpart to CHK1, which is activated by ATR and handles replication stress; the two are often conflated and should not be.

Clinically, CHEK2 matters mainly through germline variation. The truncating allele 1100delC and other loss-of-function variants confer moderately increased risk of breast cancer and, less strongly, prostate and colorectal cancer. Truncating CHEK2 variants were originally reported in families with a Li-Fraumeni-like presentation, which is where the gene's reputation as a p53-pathway tumour suppressor began.

## What is uncertain

How much p53 activation actually requires CHK2 is contested, and the two best experiments disagree. Chk2-deficient mice are radioresistant with defective p53-mediated transcription, implying CHK2 is important; somatic knockout of CHEK2 in human colorectal cancer cells left p53 responses intact, implying it is not. The S20 phosphorylation model is drawn in nearly every pathway diagram, but whether that site is necessary for stabilisation is disputed, and ATM phosphorylates p53 at S15 without CHK2's help. The germline story has also shifted: the Li-Fraumeni attribution has largely not held up, CHEK2 is now classed as a moderate-penetrance gene, and the effect of many missense variants remains uncertain. For Tahoe-100M the practical caveat is that CHK2 activity is set by phosphorylation and dimerisation, so an mRNA level is a weak proxy for how much of the kinase is actually working.

## References

- Matsuoka, Huang & Elledge, 1998, Science — linked ATM to cell-cycle regulation through the CHK2 kinase.
- Bell et al., 1999, Science — reported heterozygous germline CHEK2 mutations in Li-Fraumeni syndrome.
- Hirao et al., 2000, Science — DNA-damage-induced activation of p53 by the checkpoint kinase Chk2.
- Takai et al., 2002, The EMBO Journal — Chk2-deficient mice are radioresistant and show defective p53-mediated transcription.
- Jallepalli et al., 2003, Journal of Biological Chemistry — CHEK2 knockout in human cancer cells left p53 responses intact, the main counterweight to the mouse result.
- Meijers-Heijboer et al., 2002, Nature Genetics — established CHEK2*1100delC as a low-penetrance breast cancer susceptibility allele.
- Zannini, Delia & Buscemi, 2014, Journal of Molecular Cell Biology — review of CHK2 in the DNA damage response.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.62× (z +16.4, q 0e+00, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 1.23× (z +3.4, q 0.032, up in 8 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 7 lines (SW480 4.23×, SW1417 3.65×, KATO III 3.56×, A498 2.78×, …; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 2.79×, NCI-H460 2.45×, RKO 2.98×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SW480 4.57×, SW1417 3.27×; ⚠ cell-cycle shift, explains ~29% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 2.38×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.539× (z -10.1, q 4e-21, down in 26 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.725× (z -7.7, q 4e-12, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP192]] (+0.72, fdr 7e-06), [[L2HGDH]] (+0.69, fdr 1e-05), [[UBE2T]] (+0.68, fdr 1e-05); moves opposite to [[RNF6]] (-0.64, fdr 2e-05), [[PDCD6IP-DT]] (-0.64, fdr 1e-05), [[ACYP2]] (-0.62, fdr 3e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11452.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 7 lines (SW480 4.23×, SW1417 3.65×, KATO III 3.56×, A498 2.78×, …; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 2.79×, NCI-H460 2.45×, RKO 2.98×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SW480 4.57×, SW1417 3.27×; ⚠ cell-cycle shift, explains ~29% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 2.38×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.62×** | +16.4 | 0e+00 | 42/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.27×** | +13.9 | 1e-41 | 42/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.09×** | +12.5 | 8e-34 | 41/48 (SW480, SW1417, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.68×** | +8.8 | 3e-16 | 31/47 (J82, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.37×** | +5.4 | 9e-06 | 23/48 (HT-29, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.32×** | +4.7 | 3e-04 | 19/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.31×** | +4.6 | 3e-04 | 21/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.27×** | +4.0 | 0.004 | 19/48 (NCI-H23, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.23×** | +3.6 | 0.022 | 14/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.032 | 8/48 (Hs 766T, SHP-77, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.032 | 8/48 (Panc 03.27, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.4 | 0.032 | 12/48 (SW1417, SW480, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.22×** | +3.3 | 0.039 | 13/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.22×** | +3.3 | 0.042 | 16/48 (KATO III, C-33 A, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.087 | 9/48 (HT-29, A498, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11452.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.539×** | -10.1 | 4e-21 | 26/37 (HS-578T, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -7.7 | 4e-12 | 32/47 (NCI-H460, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.657×** | -6.6 | 9e-09 | 22/41 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.695×** | -6.2 | 1e-07 | 25/44 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.777×** | -6.0 | 2e-07 | 29/48 (J82, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.739×** | -5.1 | 3e-05 | 25/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.765×** | -4.3 | 0.001 | 17/48 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.775×** | -4.2 | 0.002 | 20/48 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.798×** | -3.8 | 0.008 | 16/48 (A-427, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.801×** | -3.8 | 0.009 | 20/47 (KATO III, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.814×** | -3.5 | 0.025 | 18/48 (A-427, HCT15, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.816×** | -3.4 | 0.026 | 16/48 (NCI-H2347, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **0.817×** | -3.4 | 0.026 | 16/48 (NCI-H2030, SW 1271, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.821×** | -3.3 | 0.032 | 9/48 (hTERT-HPNE, Hs 766T, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.870× | -3.3 | 0.032 | 19/48 (A498, SNU-1, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.833×** | -3.1 | 0.070 | 16/48 (Panc 03.27, HCT15, …) | rises with dose |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 0.835× | -3.0 | 0.077 | 12/48 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 163 | 3 (2 ⚠) | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.38× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -21.0) |
| [[A498 (line)]] | wt | 50.1 | 2 (2 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.78× (z +10.4) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -8.7) |
| [[SW1417 (line)]] | alt | 36.5 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.65× (z +11.7) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 5 µM 0.331× (z -9.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 27.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.45× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Selinexor (drug)]] 5 µM 0.339× (z -11.7) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW480 (line)]] | alt | 22.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.57× (z +15.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -11.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 38.7 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.82× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -9.9) |
| [[KATO III (line)]] | alt | 35.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.56× (z +11.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 57.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -11.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 30.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +14.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 2 (1 ⚠) | — | [[Saquinavir (drug)]] 0.5 µM 0.174× (z -9.2) |
| [[SHP-77 (line)]] | alt | 44.1 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.102× (z -9.1) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 32.8 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0662× (z -10.9) |
| [[A549 (line)]] | wt | 16.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.17× (z +9.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 45.3 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.0695× (z -9.0) |
| [[H4 (line)]] | wt | 39.4 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0629× (z -10.8) |
| [[HCT15 (line)]] | alt | 49.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -10.5) |
| [[HS-578T (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -12.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -15.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -10.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 33.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -9.6) |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -8.8) |
| [[SNU-423 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP192]] | +0.72 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[L2HGDH]] | +0.69 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[UBE2T]] | +0.68 | +0.53 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[MIS18BP1]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[CENPW]] | +0.64 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[STIL]] | +0.64 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[SLF1]] | +0.64 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[CEP152]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[TTK]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[BLM]] | +0.63 | +0.47 / +0.60 | both halves | 2e-05 | pathway: Cell Cycle Checkpoints; STRING 744 |
| [[NEIL3]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[HAUS4]] | +0.62 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF6]] | -0.64 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[PDCD6IP-DT]] | -0.64 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ACYP2]] | -0.62 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ZNF514]] | -0.62 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[HCG17]] | -0.61 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ARRDC3-AS1]] | -0.60 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[LTO1]] | -0.60 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[LINC00571]] | -0.60 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[EIF5]] | -0.59 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[FBXO30]] | -0.58 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[MMADHC-DT]] | -0.58 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[LINC00667]] | -0.57 | -0.53 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CHEK2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PBK]] | C | PBK activity raises CHEK2's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.04× lower at baseline in the lines without PBK | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-32.4, -53.3); signed map (-45.5, -38.8). **Vector** length 113, 28.7% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.51 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.56 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.60 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.6 | +16.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.6 | +13.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.8 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +3.3 | +8.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.8 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[Silodosin (drug)]] 5 µM |  | +2.2 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -7.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -5.8 | -6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | checkpoint kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:28,687,743-28,742,422 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDS1, CHK2, HuCds1, PP1425, bA444G7; previously RAD53 |
| Gene groups (HGNC) | Checkpoint kinase 2 family |
| Hallmark sets | E2F_TARGETS |
| Reactome | 21 pathways, smallest: Chk1/Chk2(Cds1) mediated inactivation of Cyclin B:Cdk1 complex; Regulation of TP53 Activity through Methylation; Regulation of TP53 Degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [O96017](https://www.uniprot.org/uniprotkb/O96017) (Serine/threonine-protein kinase Chk2):

> Serine/threonine-protein kinase which is required for checkpoint-mediated cell cycle arrest, activation of DNA repair and apoptosis in response to the presence of DNA double-strand breaks. May also negatively regulate cell cycle progression during unperturbed cell cycles. Following activation, phosphorylates numerous effectors preferentially at the consensus sequence [L-X-R-X-X-S/T]. Regulates cell cycle checkpoint arrest through phosphorylation of CDC25A, CDC25B and CDC25C, inhibiting their …

**Summary**, from NCBI Gene [11200](https://www.ncbi.nlm.nih.gov/gene/11200):

> In response to DNA damage and replication blocks, cell cycle progression is halted through the control of critical cell cycle regulators. The protein encoded by this gene is a cell cycle checkpoint regulator and putative tumor suppressor. It contains a forkhead-associated protein interaction domain essential for activation in response to DNA damage and is rapidly phosphorylated in response to replication blocks and DNA damage. When activated, the encoded protein is known to inhibit CDC25C …

**Accessions** — [HGNC:16627](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16627) · Entrez [11200](https://www.ncbi.nlm.nih.gov/gene/11200) · UniProt [O96017](https://www.uniprot.org/uniprotkb/O96017) · Ensembl [ENSG00000183765](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183765)

## Data

Gene col 11452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11452); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11452]; `tensor/DDL_lfc|DDL_z.npy` [11452]; `embed/gene_vectors.npy` [11452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11452 or target_col == 11452). Every well: [[CHEK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/CHEK2.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
