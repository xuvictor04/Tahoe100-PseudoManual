---
symbol: "RRM2B"
type: "gene"
col: 533
ensembl_id: "ENSG00000048392"
name: "ribonucleotide reductase regulatory TP53 inducible subunit M2B"
location: "8q22.3"
module: 62
arm: "+"
pooled_cpm: 55.16
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# RRM2B

*ribonucleotide reductase regulatory TP53 inducible subunit M2B* — 8q22.3

> [!summary] In one line
> RRM2B encodes p53R2, the p53-inducible small subunit of ribonucleotide reductase, which supplies deoxyribonucleotides for DNA repair and for mitochondrial DNA synthesis in cells that are not in S phase.

## What it is

Ribonucleotide reductase makes the deoxyribonucleotides that DNA synthesis consumes, and it is the committed step: no dNTPs, no replication and no repair. The enzyme pairs a large catalytic subunit, RRM1, with a small subunit supplying the tyrosyl radical. Mammals have two alternative small subunits, and the difference between them is the whole point of this gene. RRM2 is the S-phase subunit: cell-cycle regulated, abundant in dividing cells, destroyed on exit from mitosis. RRM2B — p53R2 — is the damage-inducible, quiescence-competent one, transcribed from a p53-responsive promoter at 8q22.3.

It was identified as a p53 target supplying dNTPs for repair, and reported shortly afterwards as responsive to p73 as well. The consequence is that a non-dividing cell retains a route to dNTPs: RRM1 pairs with p53R2 instead of RRM2, and the pathway is switched on by damage rather than by the cell cycle.

The genetics have shifted where the emphasis sits. *Rrm2b*-null mice die early with severe renal failure and depleted dNTP pools. In humans, biallelic loss of function causes an mtDNA depletion syndrome — severe infantile encephalomyopathy with tubulopathy — and heterozygous truncating variants cause autosomal-dominant progressive external ophthalmoplegia with multiple mtDNA deletions. The unifying explanation is that mitochondrial DNA replicates on its own schedule, so it depends on the dNTP supply route that does not require S phase. RRM2B is therefore, in practice, a mitochondrial maintenance gene as much as a damage-response gene.

## What is uncertain

What p53R2 is *for* physiologically is not settled. The original framing — a p53-controlled dNTP supply dedicated to repairing damaged nuclear DNA — sits uneasily with the human and mouse genetics, which read much more like a constitutive housekeeping requirement for mitochondrial and post-mitotic dNTP pools. Both can be true, but the relative weight is genuinely open, and the field's centre of gravity has moved toward the mitochondrial role. Whether p53R2 acts inside mitochondria or supplies a cytosolic pool they import was contested; the balance of evidence favours cytosolic reduction with transport of the product, so "mitochondrial ribonucleotide reductase" is misleading shorthand. Whether RRM2B is net tumour-suppressive is also unresolved: supplying dNTPs supports repair in cancer cells too, and reported associations between RRM2B level and outcome run in both directions depending on tumour type and treatment. Finally, the disease variants are loss-of-function; nothing about them says what a modest change in RRM2B transcript level does to dNTP pools, which are buffered and allosterically controlled.

## References

- Tanaka et al., 2000, Nature — identified RRM2B/p53R2 as a ribonucleotide reductase subunit gene in a p53-dependent checkpoint response to DNA damage.
- Nakano et al., 2000, Oncogene — showed the gene is a transcriptional target of both p53 and p73.
- Kimura et al., 2003, Nature Genetics — *Rrm2b*-null mice develop severe renal failure with attenuated dNTP pools.
- Bourdon et al., 2007, Nature Genetics — RRM2B mutation causes severe mitochondrial DNA depletion in humans.
- Tyynismaa et al., 2009, American Journal of Human Genetics — a heterozygous truncating RRM2B mutation causes autosomal-dominant progressive external ophthalmoplegia with multiple mtDNA deletions.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +19.6, q 0e+00, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.734× (z -7.1, q 5e-10, down in 30 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.804× (z -5.0, q 1e-04, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EDA2R]] (+0.77, fdr 7e-06), [[FDXR]] (+0.73, fdr 7e-06), [[ZMAT3]] (+0.72, fdr 7e-06); moves opposite to [[VKORC1L1]] (-0.53, fdr 2e-05), [[SMAGP]] (-0.46, fdr 3e-05), [[POLR1E]] (-0.45, fdr 1e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); 1 goes from it, the strongest it → [[FBXO22]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +19.6 | 0e+00 | 37/46 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +12.4 | 1e-32 | 33/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +11.7 | 3e-29 | 32/46 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +10.2 | 2e-22 | 27/47 (A498, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.43×** | +8.3 | 1e-14 | 24/47 (Hs 766T, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +8.2 | 2e-14 | 30/47 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.42×** | +8.0 | 9e-14 | 27/47 (HEC-1-A, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +7.8 | 5e-13 | 27/47 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +7.5 | 5e-12 | 28/47 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +7.0 | 1e-10 | 28/46 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +7.0 | 1e-10 | 25/46 (A498, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.33×** | +6.5 | 3e-09 | 26/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.35×** | +6.4 | 5e-09 | 25/44 (RPMI-7951, C32, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.32×** | +6.4 | 6e-09 | 28/46 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | composition shift |
| [[Amsacrine (drug)]] 5 µM |  | 1.20× | +5.9 | 1e-07 | 19/47 (RKO, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +5.4 | 2e-06 | 22/47 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +4.8 | 4e-05 | 25/48 (A498, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.8 | 5e-05 | 24/47 (A498, RKO, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.002 | 18/47 (AsPC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.8 | 0.003 | 13/47 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.8 | 0.003 | 14/47 (H4, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.018 | 10/47 (A498, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 533.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.734×** | -7.1 | 5e-10 | 30/47 (SW 900, A549, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.804×** | -5.0 | 1e-04 | 24/47 (C32, LOX-IMVI, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.851× | -3.7 | 0.027 | 16/47 (NCI-H1792, NCI-H661, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.799×** | -3.7 | 0.027 | 15/47 (NCI-H661, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.735×** | -3.7 | 0.027 | 13/47 (RPMI-7951, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.855× | -3.6 | 0.027 | 16/47 (CHP-212, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.808×** | -3.5 | 0.035 | 16/47 (RPMI-7951, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.864× | -3.3 | 0.073 | 16/47 (RKO, NCI-H1792, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.821×** | -3.2 | 0.073 | 11/47 (SK-MEL-2, HCT15, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | 0.774× | -3.1 | 0.11 | 13/47 (H4, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | 0.775× | -3.0 | 0.11 | 8/46 (MIA PaCa-2, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.878× | -3.0 | 0.11 | 15/47 (A549, NCI-H23, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 0.777× | -3.0 | 0.11 | 10/47 (SW480, A498, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 137 | 15 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +18.0) | — |
| [[NCI-H460 (line)]] | wt | 57.1 | 14 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +19.9) | — |
| [[RKO (line)]] | wt | 116 | 14 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +18.9) | — |
| [[A549 (line)]] | wt | 107 | 10 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.52× (z +14.0) | — |
| [[A-172 (line)]] | wt | 107 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 4.08× (z +12.7) | — |
| [[LoVo (line)]] | wt | 39.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +14.1) | — |
| [[LS 180 (line)]] | wt | 39.5 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 73.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +18.5) | — |
| [[HepG2_C3A (line)]] | wt | 53.3 | 4 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +10.5) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.36× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 112 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 2.92× (z +12.0) | [[Auranofin (drug)]] 5 µM 0.452× (z -9.0) |
| [[SW48 (line)]] | wt | 48.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 4.42× (z +9.6) | — |
| [[C32 (line)]] | wt | 147 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +16.3) | [[Auranofin (drug)]] 5 µM 0.373× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 26.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.2) | [[XRK3F2 (drug)]] 0.5 µM 0.175× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 57.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +19.2) | — |
| [[SW480 (line)]] | alt | 39.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +15.8) | — |
| [[A-427 (line)]] | wt | 52.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 2.64× (z +9.5) | — |
| [[H4 (line)]] | wt | 91.8 | 2 | 0 | [[Selinexor (drug)]] 5 µM 2.72× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 22.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 71.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 55.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.5) | [[Digitoxin (drug)]] 5 µM 0.295× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 89.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 5.25× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 38.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +19.9) | — |
| [[Hs 766T (line)]] | wt | 41.3 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.111× (z -9.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 84.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.2) | — |
| [[J82 (line)]] | alt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +14.1) | — |
| [[NCI-H661 (line)]] | alt | 61.4 | 0 | 1 | — | [[Ralimetinib dimesylate (drug)]] 0.5 µM 0.0739× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 47.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.512× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 38.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 52.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.80× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 59.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 59.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.7) | — |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDA2R]] | +0.77 | +0.62 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[FDXR]] | +0.73 | +0.66 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ZMAT3]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 | STRING 495 |
| [[ACTA2]] | +0.71 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[TP53INP1]] | +0.70 | +0.56 / +0.71 | both halves | 1e-05 | STRING 412 |
| [[SPATA18]] | +0.69 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[ANKRA2]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[PTCHD4]] | +0.68 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[BTG2]] | +0.68 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[MDM2]] | +0.68 | +0.56 / +0.72 | both halves | 1e-05 | STRING 750 |
| [[GRIN2C]] | +0.68 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[APOBEC3C]] | +0.67 | +0.40 / +0.74 | both halves | 5e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VKORC1L1]] | -0.53 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[SMAGP]] | -0.46 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[POLR1E]] | -0.45 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[TMEM241]] | -0.45 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[SLC19A1]] | -0.45 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[TELO2]] | -0.44 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[FANCA]] | -0.44 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[RRP7BP-1]] | -0.44 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[PRIM2]] | -0.44 | -0.50 / -0.33 | both halves | 1e-04 | STRING 699 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 1, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity strengthens RRM2B's drug response | recorded loss-of-function mutation of TP53 in 30 lines vs 17 not recorded | the TP53-altered lines respond 0.85× as strongly (z diff +0.38); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.23x vs 3.44x (z diff +6.5) | 0.018 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity raises RRM2B's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.86× lower at baseline in the lines without PTCHD4 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[PINCR]] | B | PINCR activity raises RRM2B's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.65× lower at baseline in the lines without PINCR | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[EDA2R]] | B | EDA2R activity raises RRM2B's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.68× lower at baseline in the lines without EDA2R | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[TOP2A]] | B | TOP2A activity lowers RRM2B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens RRM2B's drug response | lines that do not express PINCR (28) vs lines expressing it (19) | the lines without PINCR respond 0.84× as strongly (z diff +0.43); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.25x vs 2.99x (z diff +5.3) | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; artifact flags |
| [[FAS]] | B | FAS activity raises RRM2B's level | lines that do not express FAS (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without FAS | 0.050 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[PTCHD4]] | B | PTCHD4 activity strengthens RRM2B's drug response | lines that do not express PTCHD4 (32) vs lines expressing it (15) | the lines without PTCHD4 respond 1.01× as strongly (z diff +0.13); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.36x vs 3.18x (z diff +6.1) | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; target measured in part of the lines; both ways; artifact flags |
| [[ACTA2]] | B | ACTA2 activity raises RRM2B's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.40× lower at baseline in the lines without ACTA2 | 0.052 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO22]] | C | RRM2B's natural level strengthens FBXO22's drug response | RRM2B's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.05; direction not clear | 0.031 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.789). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.2, 36.4); signed map (42.3, -24.1). **Vector** length 122, 34.7% of its response variance represented; |z| ≥ 3 in 1,338 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 pathway* (hallmark, mean cos +0.56 to 26); *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.59 to 6); *apoptosis* (hallmark, mean cos +0.62 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.9 | +7.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +10.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.3 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +4.2 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +19.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.6 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +2.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.5 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.7 | +7.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.6 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ribonucleotide reductase regulatory TP53 inducible subunit M2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:102,204,502-102,238,961 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p53R2 |
| Gene groups (HGNC) | Ribonucleotide reductase subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 4 pathways, smallest: Interconversion of nucleotide di- and triphosphates; TP53 Regulates Metabolic Genes; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7LG56](https://www.uniprot.org/uniprotkb/Q7LG56) (Ribonucleoside-diphosphate reductase subunit M2 B):

> Part of the ribonucleotide reductase (RNR) complex composed of a catalytic large alpha subunit (RRM1/RR1) and a small beta subunit (RRM2B/RR2B) required for DNA synthesis. The active form is an alpha2beta2 heterotetramer in which the RR1-containing subunits (alpha2) catalyze reduction of ribonucleotides to deoxyribonucleotides, while the RRM2B-containing subunits (beta2) provide the diferric-tyrosyl radical cofactor required for catalysis and radical transfer. Mechanistically, RRM2B-containing …

**Summary**, from NCBI Gene [50484](https://www.ncbi.nlm.nih.gov/gene/50484):

> This gene encodes the small subunit of a p53-inducible ribonucleotide reductase. This heterotetrameric enzyme catalyzes the conversion of ribonucleoside diphosphates to deoxyribonucleoside diphosphates. The product of this reaction is necessary for DNA synthesis. Mutations in this gene have been associated with autosomal recessive mitochondrial DNA depletion syndrome, autosomal dominant progressive external ophthalmoplegia-5, and mitochondrial neurogastrointestinal encephalopathy. Alternatively …

**Accessions** — [HGNC:17296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17296) · Entrez [50484](https://www.ncbi.nlm.nih.gov/gene/50484) · UniProt [Q7LG56](https://www.uniprot.org/uniprotkb/Q7LG56) · Ensembl [ENSG00000048392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048392)

## Data

Gene col 533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 533); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 533]; `tensor/DDL_lfc|DDL_z.npy` [533]; `embed/gene_vectors.npy` [533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 533 or target_col == 533). Every well: [[RRM2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/RRM2B.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
