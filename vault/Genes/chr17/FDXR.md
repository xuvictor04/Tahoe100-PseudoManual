---
symbol: "FDXR"
type: "gene"
col: 8434
ensembl_id: "ENSG00000161513"
name: "ferredoxin reductase"
location: "17q25.1"
module: 62
arm: "+"
pooled_cpm: 16.08
n_lines_expressing: 42
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 15
direction_downstream: 17
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# FDXR

*ferredoxin reductase* — 17q25.1

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> FDXR encodes mitochondrial NADPH:ferredoxin reductase, the entry point for electrons into the ferredoxin system that supplies steroidogenic cytochromes P450 and iron-sulfur cluster assembly; it is a direct p53 target and the strongest known blood-transcript biomarker of radiation dose.

## What it is

FDXR is a FAD-containing flavoprotein of the mitochondrial inner compartment, also called adrenodoxin reductase or ferredoxin reductase (FR). It accepts a hydride from NADPH and passes single electrons to the small iron-sulfur proteins ferredoxin 1 and ferredoxin 2. Through FDX1 (adrenodoxin) this chain supplies the mitochondrial cytochromes P450 — CYP11A1 for the first committed step of steroidogenesis, CYP11B1/B2, and the vitamin D hydroxylases. Through FDX2 it supplies the core iron-sulfur cluster assembly machinery. That second branch is why FDXR, despite its adrenal-sounding name, is expressed in essentially every cell.

Its place in p53 biology came out of a differential screen for genes induced by p53 after 5-fluorouracil, where it was one of very few hits. Raising FR sensitised cells to 5-FU and suppressing it protected them, and the proposed mechanism was generation of oxidative stress in mitochondria downstream of p53. Later work made the relationship reciprocal rather than one-way: FDXR loss raises iron regulatory protein 2, which in turn represses p53 (and, by destabilising TP73 mRNA, p73), so FDXR and p53 sit in a feedback loop routed through iron homeostasis, and FDXR is required for p53-dependent tumour suppression in that model.

FDXR's most practical claim is as a dosimeter. It is the best stand-alone transcriptional biomarker of ionising radiation exposure in human blood, with a usable dose-response extending to low and partial-body exposures — a direct consequence of its being a steep, reliable p53 target in lymphocytes. Clinically, biallelic loss-of-function FDXR variants cause a mitochondriopathy with optic atrophy and auditory neuropathy, consistent with loss of the ISC branch rather than the steroidogenic one.

## What is uncertain

Whether FDXR induction produces ROS, which is the mechanism originally proposed for its contribution to p53-dependent death, is not settled; a reductase feeding iron-sulfur cluster assembly could as easily lower oxidative stress as raise it, and the two readings have not been cleanly separated in one system. The feedback loop onto p53 means FDXR is both a target and a modulator of the pathway, so treating its level as a pure readout is an approximation — defensible for a 24 h mRNA measurement, less so if protein-level or chronic effects are in play. Because part of its expression serves constitutive ISC biogenesis, FDXR carries a real housekeeping floor, which damps its fold-change relative to targets with no basal function; absolute and relative induction will disagree about its rank. Finally, the biodosimetry literature finds that specific FDXR transcript variants carry the signal, and a 3′-biased short-read assay collapses them into one number.

## References

- Hwang et al., 2001, Nature Medicine — identified FDXR as one of few genes induced by p53 after 5-fluorouracil and showed its level modulates p53-dependent apoptosis in colorectal cancer cells.
- Zhang et al., 2017, Genes & Development — showed ferredoxin reductase is critical for p53-dependent tumour suppression via iron regulatory protein 2, establishing an FDXR–p53 feedback loop through iron homeostasis.
- O'Brien et al., 2018, Scientific Reports — demonstrated FDXR as a biomarker of radiation exposure in vivo, with a dose-response at low and partial-body doses.
- Peng et al., 2017, Human Molecular Genetics — reported biallelic FDXR mutations in 17 individuals from 13 unrelated families causing a mitochondriopathy with optic atrophy, with reduced ferredoxin reductase activity in patient fibroblasts rescued by wild-type FDXR.
- Paul et al., 2017, American Journal of Human Genetics — independently found biallelic FDXR variants in four families with auditory neuropathy and optic atrophy, with pathogenicity established by complementation in yeast.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.07× (z +10.8, q 3e-24, up in 33 of 33 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.06× (z +9.1, q 1e-17, up in 31 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 0.683× (z -3.8, q 0.043, down in 16 of 38 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.694× (z -3.7, q 0.048, down in 17 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.156×, A-172 0.124×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0800×, NCI-H23 0.200×); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (CHP-212 0.0367×, hTERT-HPNE 0.115×; ⚠ toxic); [[Azithromycin (hydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0553×); [[Digitoxin (drug)]] 0.5 µM in 1 line (C-33 A 0.0536×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRIN2C]] (+0.84, fdr 7e-06, ⚠ same locus), [[EDA2R]] (+0.79, fdr 7e-06), [[DDB2]] (+0.78, fdr 7e-06), [[ZMAT3]] (+0.75, fdr 7e-06); moves opposite to [[MTAP]] (-0.48, fdr 4e-05), [[DIAPH2]] (-0.48, fdr 5e-05), [[EHBP1]] (-0.46, fdr 2e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); 17 go from it, the strongest it → [[POLH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8434.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.07×** | +10.8 | 3e-24 | 33/33 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.73×** | +10.0 | 4e-21 | 22/39 (SW480, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +9.1 | 1e-17 | 31/39 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.45×** | +8.9 | 5e-17 | 19/39 (KATO III, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +6.8 | 1e-09 | 25/39 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.80×** | +5.6 | 2e-06 | 23/37 (A549, NCI-H460, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.74×** | +5.5 | 3e-06 | 22/39 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.73×** | +5.5 | 3e-06 | 19/39 (SW480, KATO III, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.80×** | +5.4 | 4e-06 | 22/36 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.59×** | +4.5 | 5e-04 | 21/38 (A549, NCI-H460, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.85×** | +4.4 | 6e-04 | 13/35 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.003 | 18/38 (A549, RKO, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +3.8 | 0.006 | 11/35 (Panc 03.27, SNU-423, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.7 | 0.009 | 3/40 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.009 | 16/38 (SNU-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.058 | 16/38 (NCI-H460, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM |  | **1.36×** | +3.0 | 0.068 | 11/38 (A549, A-427, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.081 | 15/37 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.091 | 15/40 (A549, NCI-H460, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.091 | 16/40 (NCI-H460, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8434.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.156×, A-172 0.124×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0800×, NCI-H23 0.200×); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (CHP-212 0.0367×, hTERT-HPNE 0.115×; ⚠ toxic); [[Azithromycin (hydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0553×); [[Digitoxin (drug)]] 0.5 µM in 1 line (C-33 A 0.0536×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.683×** | -3.8 | 0.043 | 16/38 (A-427, A498, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.685×** | -3.8 | 0.043 | 14/39 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.694×** | -3.7 | 0.048 | 17/38 (C-33 A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.703×** | -3.5 | 0.057 | 19/37 (H4, A549, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.777× | -3.3 | 0.10 | 11/38 (A-427, NCI-H23, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.717× | -3.2 | 0.12 | 15/38 (COLO 205, NCI-H661, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.728× | -3.2 | 0.12 | 19/38 (hTERT-HPNE, NCI-H23, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8434. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 58.0 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 7.86× (z +10.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 3.94× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 25.3 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +11.4) | — |
| [[A-427 (line)]] | wt | 46.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.75× (z +8.7) ⚠ cell-cycle shift, explains ~40% of this change | [[Dinaciclib (drug)]] 5 µM 0.156× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 64.2 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0367× (z -10.1) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 0.0561× (z -8.8) |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.101× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 43.6 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0800× (z -10.3) |
| [[KATO III (line)]] | alt | 10.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 7.38× (z +9.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 49.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +14.6) | — |
| [[RKO (line)]] | wt | 24.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 21.1 | 2 | 0 | [[Selinexor (drug)]] 5 µM 8.57× (z +9.7) | — |
| [[SW480 (line)]] | alt | 12.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.96× (z +10.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 35.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 8.24 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0536× (z -10.4) |
| [[COLO 205 (line)]] | alt | 6.68 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0513× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0553× (z -11.5) |
| [[LoVo (line)]] | wt | 27.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.39× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 34.1 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.21× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.200× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 6.39 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0647× (z -9.2) |
| [[SW1417 (line)]] | alt | 10.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.59× (z +9.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW48 (line)]] | wt | 32.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 8.96× (z +9.1) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[AN3 CA (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8434), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRIN2C]] | +0.84 | +0.74 / +0.86 | both halves | 7e-06 | ⚠ same locus (1.0 kb, same strand: neighbours can correlate without regulation) |
| [[EDA2R]] | +0.79 | +0.72 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[DDB2]] | +0.78 | +0.74 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 730 |
| [[ZMAT3]] | +0.75 | +0.68 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 485 |
| [[PINCR]] | +0.74 | +0.60 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[TP53INP1]] | +0.73 | +0.62 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[RRM2B]] | +0.73 | +0.66 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[PIDD1]] | +0.72 | +0.62 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[MDM2]] | +0.72 | +0.68 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 505 |
| [[PPM1D]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[MIR34AHG]] | +0.71 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[PTCHD4]] | +0.70 | +0.57 / +0.76 | both halves | 8e-06 |  |
| [[SPATA18]] | +0.70 | +0.51 / +0.80 | both halves | 1e-05 | STRING 412 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTAP]] | -0.48 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[DIAPH2]] | -0.48 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[EHBP1]] | -0.46 | -0.50 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 2, B 12, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity raises FDXR's level | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | 3.95× lower at baseline in the TP53-altered lines | 4e-04 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[TP53]] | A | TP53 activity strengthens FDXR's drug response | recorded loss-of-function mutation of TP53 in 23 lines vs 17 not recorded | the TP53-altered lines respond 0.74× as strongly (z diff +0.75); strongest at Idarubicin (hydrochloride) 5 µM: 1.59x vs 3.62x (z diff +4.3) | 6e-04 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; lower baseline (lost expression?); both ways; artifact flags |
| [[PINCR]] | B | PINCR activity raises FDXR's level | lines that do not express PINCR (29) vs lines expressing it (21) | 3.22× lower at baseline in the lines without PINCR | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[TOP2A]] | B | TOP2A activity lowers FDXR's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.9% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity raises FDXR's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 2.80× lower at baseline in the lines without PTCHD4 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[PINCR]] | B | PINCR activity strengthens FDXR's drug response | lines that do not express PINCR (21) vs lines expressing it (19) | the lines without PINCR respond 0.70× as strongly (z diff +0.85); strongest at Idarubicin (hydrochloride) 5 µM: 1.61x vs 3.28x (z diff +3.8) | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; artifact flags |
| [[EDA2R]] | B | EDA2R activity raises FDXR's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.93× lower at baseline in the lines without EDA2R | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[CYFIP2]] | B | CYFIP2 activity raises FDXR's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.62× lower at baseline in the lines without CYFIP2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[PURPL]] | B | PURPL activity raises FDXR's level | lines that do not express PURPL (25) vs lines expressing it (25) | 2.08× lower at baseline in the lines without PURPL | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[ACTA2]] | B | ACTA2 activity raises FDXR's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 2.26× lower at baseline in the lines without ACTA2 | 0.044 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[DDX3Y]] | B | DDX3Y activity raises FDXR's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without DDX3Y | 0.056 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[PRKY]] | B | PRKY activity raises FDXR's level | lines that do not express PRKY (30) vs lines expressing it (20) | 1.84× lower at baseline in the lines without PRKY | 0.057 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1 |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 12, C 5. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLH]] | B | FDXR activity raises POLH's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without FDXR | 0.012 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[ZMAT3]] | B | FDXR activity raises ZMAT3's level | lines that do not express FDXR (8) vs lines expressing it (42) | 2.54× lower at baseline in the lines without FDXR | 0.017 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[CYFIP2]] | B | FDXR activity raises CYFIP2's level | lines that do not express FDXR (8) vs lines expressing it (42) | 3.00× lower at baseline in the lines without FDXR | 0.030 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[BLOC1S2]] | B | FDXR activity raises BLOC1S2's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without FDXR | 0.047 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[DDB2]] | B | FDXR activity raises DDB2's level | lines that do not express FDXR (8) vs lines expressing it (42) | 2.09× lower at baseline in the lines without FDXR | 0.049 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[ZNF79]] | B | FDXR activity raises ZNF79's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.25× lower at baseline in the lines without FDXR | 0.049 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[TRIAP1]] | B | FDXR activity raises TRIAP1's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without FDXR | 0.080 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[DNAI3]] | B | FDXR activity raises DNAI3's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.41× lower at baseline in the lines without FDXR | 0.081 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[TM7SF3]] | B | FDXR activity raises TM7SF3's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without FDXR | 0.083 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[RAD51C]] | B | FDXR activity raises RAD51C's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without FDXR | 0.085 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[BAX]] | B | FDXR activity raises BAX's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without FDXR | 0.086 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[NTN1]] | B | FDXR activity raises NTN1's level | lines that do not express FDXR (8) vs lines expressing it (42) | 2.03× lower at baseline in the lines without FDXR | 0.097 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.867). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.5, 36.3); signed map (42.2, -24.5). **Vector** length 116, 33.0% of its response variance represented; |z| ≥ 3 in 956 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.64 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.0 | +10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.5 | +3.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.9 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.3 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +4.0 | +5.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.8 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | +1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.1 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ferredoxin reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:74,862,497-74,873,031 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADR, AR; previously ADXR |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Mitochondrial iron-sulfur assembly components; Flavoproteins; Oxidoreductases |
| Hallmark sets | BILE_ACID_METABOLISM, APOPTOSIS, P53_PATHWAY, MTORC1_SIGNALING |
| Reactome | 13 pathways, smallest: Defective CYP11A1 causes AICSR; Electron transport from NADPH to Ferredoxin; Pregnenolone biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P22570](https://www.uniprot.org/uniprotkb/P22570) (NADPH:adrenodoxin oxidoreductase, mitochondrial):

> Serves as the first electron transfer protein in all the mitochondrial P450 systems including cholesterol side chain cleavage in all steroidogenic tissues, steroid 11-beta hydroxylation in the adrenal cortex, 25-OH-vitamin D3-24 hydroxylation in the kidney, and sterol C-27 hydroxylation in the liver (By similarity). Also acts as a ferredoxin--NADP(+) reductase essential for coenzyme Q biosynthesis: together with FDX2, transfers the electrons required for the hydroxylation reaction performed by …

**Summary**, from NCBI Gene [2232](https://www.ncbi.nlm.nih.gov/gene/2232):

> This gene encodes a mitochondrial flavoprotein that initiates electron transport for cytochromes P450 receiving electrons from NADPH. Multiple alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:3642](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3642) · Entrez [2232](https://www.ncbi.nlm.nih.gov/gene/2232) · UniProt [P22570](https://www.uniprot.org/uniprotkb/P22570) · Ensembl [ENSG00000161513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161513)

## Data

Gene col 8434: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8434); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8434, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8434]; `tensor/DDL_lfc|DDL_z.npy` [8434]; `embed/gene_vectors.npy` [8434]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8434 or target_col == 8434). Every well: [[FDXR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/FDXR.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
